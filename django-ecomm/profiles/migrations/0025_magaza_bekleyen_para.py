# Generated by Django 3.1.4 on 2021-01-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_kullanici_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='magaza',
            name='bekleyen_para',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=999, null=True, verbose_name='Askıdaki para'),
        ),
    ]