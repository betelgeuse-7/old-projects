# Generated by Django 3.1.4 on 2021-01-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20210106_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='magaza',
            name='sifre',
            field=models.CharField(default='sifre', max_length=50, verbose_name='Şifre'),
        ),
    ]
