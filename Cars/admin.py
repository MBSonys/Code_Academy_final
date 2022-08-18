from django.contrib import admin
from .models import CarPoster
from Users.models import Seller


class CarPostersAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'car_model', 'car_poster_owner', 'poster_date', 'car_poster_price', 'status')
    list_filter = ('car_make', 'status')
    search_fields = ('car_make', 'car_model', 'car_poster_owner', 'poster_date', 'car_poster_price', 'car_year')
    list_editable = ['status']
    list_per_page = 10


admin.site.register(CarPoster, CarPostersAdmin)
admin.site.register(Seller)
# Register your models here.
