from django.urls import path

from . import views

urlpatterns = [
    path('', views.CarsHomePageListView.as_view(), name='index'),
    path('search/', views.search, name='search'),
]