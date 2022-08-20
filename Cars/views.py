from django.shortcuts import render, redirect
from .models import CarPoster
from django.views import generic
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


class CarsHomePageListView(generic.ListView):
    model = CarPoster
    template_name = 'index.html'
    context_object_name = "cars"
    query_to_delete = CarPoster.objects.filter(status__exact='r').all()
    query_to_delete.delete()

    def get_queryset(self):
        queryset = {
            "fresh_new": CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')[:6],
            "fresh_new_1_3": CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')[:3],
            "fresh_new_3_6": CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')[3:6],
            "highest_price_1_3": CarPoster.objects.filter(status__exact='a').all().order_by('-car_poster_price')[:3],
            "highest_price_3_6": CarPoster.objects.filter(status__exact='a').all().order_by('-car_poster_price')[3:6]
        }
        return queryset


class CarPosterDetailView(generic.DetailView):
    model = CarPoster
    template_name = 'car_detail.html'


@login_required
def profile(request):
    return render(request, 'profile.html')


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