from django.db import models


class Group(models.Model):
    group_name = models.CharField("Forume pagrindines temos pavadininas", max_length=300)
