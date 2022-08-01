from django.shortcuts import render
from .models import CarPoster


def index(request):
    num_cars = CarPoster.objects.all().count()
    num_cars_available = CarPoster.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_cars,
        'num_instances_available': num_cars_available,
    }

    return render(request, 'index.html', context=context)
