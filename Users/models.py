from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.png", upload_to="profile_pics")
    location = models.CharField("City/Country", max_length=100, null=True)
    phone_number = models.CharField("Phone Number", max_length=13, default='6xxxxxxx', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)