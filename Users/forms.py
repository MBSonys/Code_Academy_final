from .models import Seller
from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', "first_name", "last_name"]


class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['photo', 'location', 'phone_number']