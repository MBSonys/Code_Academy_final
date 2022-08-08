from django.shortcuts import render
from .models import CarPoster
from django.views import generic


class CarsHomePageListView(generic.ListView):
    model = CarPoster
    queryset = CarPoster.objects.all()
    template_name = 'index.html'
