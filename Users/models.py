from django.contrib.auth.models import User
from django.db import models


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="no-profile-picture.png", upload_to="profile_pics")

    def __str__(self):
        return self.user.username
