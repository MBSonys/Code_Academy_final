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
    queryset = list(CarPoster.objects.all())
    template_name = 'index.html'


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