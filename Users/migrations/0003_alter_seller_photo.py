# Generated by Django 4.0.5 on 2022-08-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_users_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.ImageField(default='no-profile-picture.png', upload_to='profile_pics'),
        ),
    ]
