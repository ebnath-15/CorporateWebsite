# Generated by Django 4.2 on 2023-07-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
    ]
