# Generated by Django 4.0.5 on 2022-08-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0013_carposter_read_count_carposter_sold_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carposter',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
    ]
