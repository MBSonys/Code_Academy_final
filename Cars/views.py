from django.shortcuts import render
from .models import CarPoster
from django.views import generic
from django.db.models import Q


class CarsHomePageListView(generic.ListView):
    model = CarPoster
    queryset = CarPoster.objects.all()
    template_name = 'index.html'


def search(request):
    query = request.GET.get('query')
    search_results = CarPoster.objects.filter(Q(car_make__icontains=query) | Q(car_model__icontains=query))
    return render(request, 'search.html', {'carposter': search_results, 'query': query})