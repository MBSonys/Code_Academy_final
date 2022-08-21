from django.shortcuts import render, redirect
from .models import CarPoster
from django.views import generic
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class CarPosterDetailView(LoginRequiredMixin, generic.DetailView):
    model = CarPoster
    template_name = 'car_detail.html'

    def get_object(self):
        add_view = super().get_object()
        add_view.read_count += 1
        add_view.save()
        return add_view


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


class CarByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = CarPoster
    fields = [
        'car_make',
        'car_model',
        'car_year',
        'car_engine',
        'car_millage',
        'car_fuel_type',
        'car_chassis_type',
        'car_door_number',
        'car_drive_wheel',
        'car_transmission',
        'car_color',
        'car_MOT',
        'car_weight',
        'car_vin_number',
        'car_poster_price',
        'car_photo_1',
        'car_photo_2',
        'car_photo_3',
        'car_photo_4',
        'car_photo_5',
        'car_photo_6',
        'car_photo_7',
        'car_photo_8',
        'car_photo_9',
        'car_photo_10',
        'description'
    ]
    success_url = ""
    template_name = 'add_car.html'

    def form_valid(self, form):
        form.instance.car_poster_owner = self.request.user.seller
        return super().form_valid(form)


class CarPosterByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = CarPoster
    fields = [
        'car_make',
        'car_model',
        'car_year',
        'car_engine',
        'car_millage',
        'car_fuel_type',
        'car_chassis_type',
        'car_door_number',
        'car_drive_wheel',
        'car_transmission',
        'car_color',
        'car_MOT',
        'car_weight',
        'car_vin_number',
        'car_poster_price',
        'car_photo_1',
        'car_photo_2',
        'car_photo_3',
        'car_photo_4',
        'car_photo_5',
        'car_photo_6',
        'car_photo_7',
        'car_photo_8',
        'car_photo_9',
        'car_photo_10',
        'description'
    ]
    success_url = ""
    template_name = 'add_car.html'

    def form_valid(self, form):
        form.instance.car_poster_owner = self.request.user.seller
        return super().form_valid(form)

    def test_func(self):
        carposter = self.get_object()
        return self.request.user.seller == carposter.car_poster_owner


class CarPosterByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CarPoster
    success_url = '/'
    template_name = 'user_carposter_delete.html'

    def test_func(self):
        carposter = self.get_object()
        return self.request.user.seller == carposter.car_poster_owner


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

