# Generated by Django 3.1.4 on 2021-02-22 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_auto_20210222_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kullanici',
            name='teslim_alinanlar',
        ),
    ]
