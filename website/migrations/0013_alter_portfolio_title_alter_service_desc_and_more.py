# Generated by Django 4.2 on 2023-07-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_service_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='desc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='slider',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
