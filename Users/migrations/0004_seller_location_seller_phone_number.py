# Generated by Django 4.0.5 on 2022-08-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_seller_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='City/Country'),
        ),
        migrations.AddField(
            model_name='seller',
            name='phone_number',
            field=models.CharField(blank=True, default='6xxxxxxx', max_length=13, null=True, verbose_name='Phone Number'),
        ),
    ]
