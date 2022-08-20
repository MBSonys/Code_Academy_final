from Users.models import Seller
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from tinymce.models import HTMLField
import datetime


class CarPoster(models.Model):
    car_make = models.CharField("Gamintojas", max_length=200, help_text="Automobilio gamintojo pavadinimas")
    car_model = models.CharField("Modelis", max_length=200, help_text="Automobilio gamintojo modelis")
    car_year = models.DateField("Gamybos metai", auto_now=False, help_text="Automobilio pagaminimo metai")
    car_engine = models.CharField(
        "Variklis",
        max_length=200,
        help_text="Automobilio darbinis tūris ir sutrumpintas variklio pavadinimas"
    )
    car_millage = models.IntegerField("Automobilio rida", help_text="Automobilio nuvažiotas kilometražas (KM)")
    car_fuel_type = models.CharField("Kūro tipas", max_length=20, help_text="Automobilio variklio kūro tipas")
    car_chassis_type = models.CharField("Kebulo tipas", max_length=100, help_text="Automobilio kebulo tipas/forma")
    car_door_number = models.CharField("Durų skaičius", max_length=10, null=True, help_text="Automobilio dūrų skaičius")
    car_drive_wheel = models.CharField(
        "Varantieji ratai",
        max_length=30,
        null=True,
        help_text="Automobilio varantieji ratai"
    )
    car_transmission = models.CharField("Pavarų dėžė", max_length=50, help_text="Automobilio pavarų dežės tipas")
    car_color = models.CharField("Spalva", max_length=100, help_text="Automobilio kebulo spalva")
    car_MOT = models.DateField("Tech. apžiūra iki", help_text="Automobilio techninės apžiūros pabaigos data")
    car_weight = models.IntegerField("Automobilio masė", help_text="Automobilio nuosava masė")
    car_vin_number = models.CharField(
        "Automobilio numeris (VIN)",
        max_length=30,
        help_text="Automobilio kebulo numeris/indentifikavimo numeris"
    )
    car_poster_owner = models.ForeignKey(Seller, on_delete=models.CASCADE)
    poster_date = models.DateTimeField("Skelbimo data", default=now, blank=True, help_text="Skelbimo sukurimo data")
    car_poster_price = models.IntegerField("Skelbimo suma", help_text="Parduodamo automobilio kaina")
    car_photo_1 = models.ImageField(
        'Skelbimo nuotrauka 1',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_2 = models.ImageField(
        'Skelbimo nuotrauka 2',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_3 = models.ImageField(
        'Skelbimo nuotrauka 3',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_4 = models.ImageField(
        'Skelbimo nuotrauka 4',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_5 = models.ImageField(
        'Skelbimo nuotrauka 5',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_6 = models.ImageField(
        'Skelbimo nuotrauka 6',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_7 = models.ImageField(
        'Skelbimo nuotrauka 7',
        upload_to='poster-photos',
        null=True,
        default = "no_car_photo.png"
    )
    car_photo_8 = models.ImageField(
        'Skelbimo nuotrauka 8',
        upload_to='poster-photos',
        null=True,
        default="no_car_photo.png"
    )
    car_photo_9 = models.ImageField(
        'Skelbimo nuotrauka 9',
        upload_to='poster-photos',
        null=True,
        default="no_car_photo.png"
    )
    car_photo_10 = models.ImageField(
        'Skelbimo nuotrauka 10',
        upload_to='poster-photos',
        null=True,
        default="no_car_photo.png"
    )
    description = HTMLField(default= "For more info Call")
    sellers_likes = models.ManyToManyField(Seller, related_name='likes')

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

    # def add_poster_sold_date(self):
    #     object_to_add_date = CarPoster.objects.filter(status__exact='s').all()
    #     object_to_add_date.sold_date = datetime.datetime.now()
    #     object_to_add_date.save()
    #
    # def delete_sold_after_48h(self):
    #     object_to_add_date = CarPoster.objects.filter(status__exact='s').all()
    #     if object_to_add_date.sold_date + datetime.timedelta(days=2) < datetime.datetime.today():
    #         object_to_add_date.delete()


