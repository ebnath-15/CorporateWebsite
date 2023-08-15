# Generated by Django 4.2 on 2023-07-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='package',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='WebsiteSettings',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='bottom_subtitle',
            new_name='bottom_sub_title',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='subtitle',
            new_name='sub_title',
        ),
        migrations.AlterField(
            model_name='slider',
            name='phone',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Package',
        ),
    ]