from django.urls import path

from . import views

urlpatterns = [
    path('', views.CarsHomePageListView.as_view(), name='index'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('<int:pk>', views.CarPosterDetailView.as_view(), name='car_detail'),
    path('all_posters/', views.CarShowAllListView.as_view(), name='all_posters'),
    path('all_posters/<int:pk>', views.CarPosterDetailView.as_view(), name='car_detail'),
]