# Generated by Django 3.1.4 on 2021-01-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210106_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bildirim',
            name='kime',
        ),
        migrations.AddField(
            model_name='bildirim',
            name='kime',
            field=models.ManyToManyField(to='profiles.Kullanici', verbose_name='Kime'),
        ),
    ]
