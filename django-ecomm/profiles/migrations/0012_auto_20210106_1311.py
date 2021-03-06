# Generated by Django 3.1.4 on 2021-01-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20210106_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='magaza',
            name='net_kazanc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=999, null=True, verbose_name='Net kazanç'),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='teslim_alinanlar',
            field=models.ManyToManyField(blank=True, related_name='teslim_alinanlar', to='profiles.Urun', verbose_name='Teslim alınan ürünler'),
        ),
    ]
