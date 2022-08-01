from Users.models import Seller
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class CarPoster(models.Model):
    car_make = models.CharField("Gamintojas", max_length=200)
    car_model = models.CharField("Modelis", max_length=200)
    car_year = models.DateField("Gamybos metai", auto_now=False)
    car_engine = models.CharField("Variklis", max_length=200)
    car_millage = models.IntegerField("Automobilio rida")
    car_fuel_type = models.CharField("Kūro tipas", max_length=20)
    car_chassis_type = models.CharField("Kebulo tipas", max_length=100)
    car_door_number = models.CharField("Durų skaičius", max_length=10, null=True)
    car_drive_wheel = models.CharField("Varantieji ratai", max_length=30, null=True)
    car_transmission = models.CharField("Pavarų dėžė", max_length=50)
    car_color = models.CharField("Spalva", max_length=100)
    car_MOT = models.DateField("Tech. apžiūra iki")
    car_weight = models.IntegerField("Automobilio masė")
    car_vin_number = models.CharField("Automobilio numeris (VIN)", max_length=30)
    car_poster_owner = models.ForeignKey(Seller, on_delete=models.CASCADE)
    poster_date = models.DateTimeField("Skelbimo data", default=now, blank=True)
    poster_sold_date = models.DateTimeField("Skelbimo pardavimo data", null=True, default=None)
    car_poster_price = models.IntegerField("Skelbimo suma", default=None)

    POSTER_STATUS = (
        ('a', 'Patvirtintas'),
        ('w', 'Laukiamas'),
        ('r', 'Atmestas'),
        ('s', 'Parduota/Neaktyvus')
    )

    status = models.CharField(
        max_length=1,
        choices=POSTER_STATUS,
        blank=True,
        default='w',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['poster_date']
        verbose_name = 'Skelbimas'
        verbose_name_plural = 'Skelbimai'

    def __str__(self):
        return f"{self.car_make} - {self.car_model} : {self.car_year} - {self.car_engine}"

    def get_absolute_url(self):
        return reverse('poster-detail', args=[str(self.id)])





