# Generated by Django 2.0.7 on 2018-08-01 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detailsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='text',
            new_name='PartySize',
        ),
    ]