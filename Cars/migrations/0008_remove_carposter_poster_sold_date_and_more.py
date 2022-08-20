# Generated by Django 4.0.5 on 2022-08-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_seller_location_seller_phone_number'),
        ('Cars', '0007_alter_carposter_car_poster_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carposter',
            name='poster_sold_date',
        ),
        migrations.AddField(
            model_name='carposter',
            name='sellers_likes',
            field=models.ManyToManyField(related_name='likes', to='Users.seller'),
        ),
    ]