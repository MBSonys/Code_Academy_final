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
    path('mycars/<int:pk>', views.CarPosterDetailView.as_view(), name='car_detail'),
    path('mycars/', views.CarPostersByUserListView.as_view(), name='my_cars'),
    path('updateprofile/', views.profile_edit, name='edit_profile'),
    path('addcar/', views.CarByUserCreateView.as_view(), name='AddCar'),
    path('<int:pk>/update', views.CarPosterByUserUpdateView.as_view(), name='UpdateCar'),
    path('mycars/<int:pk>/update', views.CarPosterByUserUpdateView.as_view(), name='UpdateCar'),
    path('<int:pk>/delete', views.CarPosterByUserDeleteView.as_view(), name='DeleteCar'),
    path('mycars/<int:pk>/delete', views.CarPosterByUserDeleteView.as_view(), name='DeleteCar'),
]