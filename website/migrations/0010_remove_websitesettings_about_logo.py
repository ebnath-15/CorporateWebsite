# Generated by Django 4.2 on 2023-07-29 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_websitesettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitesettings',
            name='about_logo',
        ),
    ]
