# Generated by Django 4.0.5 on 2022-08-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0011_alter_carposter_sold_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carposter',
            name='sold_date',
        ),
    ]
