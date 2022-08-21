from django.contrib.auth.models import User
from django.db import models


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.png", upload_to="profile_pics")
    location = models.CharField("City/Country", max_length=100, null=True)
    phone_number = models.CharField("Phone Number", max_length=13, default='6xxxxxxx', null=True, blank=True)

    def __str__(self):
        return self.user.username
