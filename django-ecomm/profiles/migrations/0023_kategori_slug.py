# Generated by Django 3.1.4 on 2021-01-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_auto_20210125_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='slug',
            field=models.CharField(blank=True, max_length=150, verbose_name='Slug'),
        ),
    ]
