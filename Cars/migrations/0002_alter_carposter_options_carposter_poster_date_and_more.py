# Generated by Django 4.0.5 on 2022-07-31 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carposter',
            options={'ordering': ['poster_date']},
        ),
        migrations.AddField(
            model_name='carposter',
            name='poster_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Skelbimo data'),
        ),
        migrations.AddField(
            model_name='carposter',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Patvirtintas'), ('w', 'Laukiamas'), ('r', 'Atmestas')], default='w', help_text='Statusas', max_length=1),
        ),
    ]
