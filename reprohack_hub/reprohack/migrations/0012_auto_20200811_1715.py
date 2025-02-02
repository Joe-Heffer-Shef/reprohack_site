# Generated by Django 3.0.7 on 2020-08-11 17:15

import django.core.validators
from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0011_auto_20200810_0137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='venue_description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='time_zone',
            field=timezone_field.fields.TimeZoneField(default='Europe/London'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reproducibility_description',
            field=models.TextField(verbose_name='Briefly describe the procedure followed/tools used to reproduce it.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reproducibility_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='On a scale of 0 to 10, how much of the paper did you manage to reproduce?'),
        ),
    ]
