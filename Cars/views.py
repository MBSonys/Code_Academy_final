from django.shortcuts import render, redirect
from .models import CarPoster
from django.views import generic
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from Users.forms import UserUpdateForm, SellerUpdateForm

class CarsHomePageListView(generic.ListView):
    model = CarPoster
    template_name = 'index.html'
    # query_to_delete = CarPoster.objects.filter(status__exact='r').all()
    # query_to_delete.delete()


class CarShowAllListView(generic.ListView):
    model = CarPoster
    context_object_name = 'all_cars'
    paginate_by = 12
    queryset = CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')
    template_name = 'car_list.html'


class CarPosterDetailView(generic.DetailView):
    model = CarPoster
    template_name = 'car_detail.html'


class CarPostersByUserListView(LoginRequiredMixin, generic.ListView):
    model = CarPoster
    context_object_name = 'user_cars'
    template_name = 'user_cars.html'
    paginate_by = 12

    def get_queryset(self):
        return CarPoster.objects.filter(
            car_poster_owner=self.request.user.seller
        ).filter(
            status__exact='a'
        ).order_by('-poster_date')


@login_required
def profile(request):
    car_count = {'number_of_user_cars': CarPoster.objects.filter(car_poster_owner=request.user.seller).filter(status__exact='a').count()}
    return render(request, 'profile.html', context=car_count)


def search(request):
    query = request.GET.get('query')
    search_results = CarPoster.objects.filter(Q(car_make__icontains=query) | Q(car_model__icontains=query))
    return render(request, 'search.html', {'carposter': search_results, 'query': query})


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeated_password = request.POST['password2']
        if password == repeated_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'This username: {username} already exist!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'This email: {email} already in use!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    context = {'new_user_name': username}
                    return render(request, 'success_register.html', context=context)
        else:
            messages.error(request, 'Passwords not the same!')
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login.html')
        ...
    # else:
    #     # Return an 'invalid login' error message.

@login_required
def profile_edit(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = SellerUpdateForm(request.POST, request.FILES, instance=request.user.seller)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = SellerUpdateForm(instance=request.user.seller)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile_update.html', context)