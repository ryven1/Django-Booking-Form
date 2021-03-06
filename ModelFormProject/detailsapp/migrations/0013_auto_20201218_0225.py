# Generated by Django 3.1.4 on 2020-12-18 02:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailsapp', '0012_auto_20201217_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='TableNo',
            field=models.IntegerField(blank=True, choices=[('1 - 2 people', '1 - 2 people'), ('2 - 3 people', '2 - 3 people'), ('3 - 3 people', '3 - 3 people'), ('4 - 5 people', '4 - 5 people'), ('5 - 5 people', '5 - 5 people'), ('6 - 5 people', '6 - 5 people'), ('7 - 5 people', '7 - 5 people'), ('8 - 5 people', '8 - 5 people'), ('9 - 6 people', '9 - 6 people'), ('10 - 6 people', '10 - 6 people')], default='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
