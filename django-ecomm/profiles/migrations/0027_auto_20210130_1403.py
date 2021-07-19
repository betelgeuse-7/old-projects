# Generated by Django 3.1.4 on 2021-01-30 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_kullanici_satin_alinanlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siparis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.PositiveIntegerField(default=1, verbose_name='Adet')),
                ('siparis_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Sipariş tarihi')),
                ('kargoya_verilme_tarihi', models.DateTimeField(blank=True, verbose_name='Kargoya verilme tarihi')),
                ('teslim_alinma_tarihi', models.DateTimeField(blank=True, verbose_name='Teslim alınma tarihi')),
                ('tamamlandi', models.BooleanField(default=False, verbose_name='Tamamlandı')),
                ('satici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.magaza', verbose_name='Satıcı')),
                ('satin_alan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.kullanici', verbose_name='Satın alan')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.urun', verbose_name='Ürün')),
            ],
        ),
        migrations.AddField(
            model_name='kullanici',
            name='siparisler',
            field=models.ManyToManyField(to='profiles.Siparis', verbose_name='Siparişler'),
        ),
        migrations.AddField(
            model_name='magaza',
            name='siparisler',
            field=models.ManyToManyField(to='profiles.Siparis', verbose_name='Siparişler'),
        ),
    ]
