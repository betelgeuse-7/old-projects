# Generated by Django 3.1.4 on 2021-01-06 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_yorum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='ad',
            field=models.CharField(max_length=100, verbose_name='Kategori adı'),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='kayit_tarihi',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Kayıt tarihi'),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='profil_fotografi',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/kullanici_profil_fotograflari', verbose_name='Profil fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='sepet',
            field=models.ManyToManyField(blank=True, null=True, to='profiles.Urun', verbose_name='Sepet'),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='toplam_harcanan_para',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999, verbose_name='Toplam harcanan para'),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='ad',
            field=models.CharField(max_length=100, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='brut_kazanc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=999, null=True, verbose_name='Brüt kazanç (Site komisyonu hariç)'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='kayit_tarihi',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Kayıt tarihi'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='ortalama_puan',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='Ortalama puan'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='profil_fotografi',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/magaza_profil_fotograflari', verbose_name='Fotoğraf'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='tanitim',
            field=models.TextField(verbose_name='Mağaza tanıtım yazısı'),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='urunler',
            field=models.ManyToManyField(blank=True, null=True, to='profiles.Urun', verbose_name='Ürünler'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='aciklama',
            field=models.TextField(verbose_name='Ürün açıklaması'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='ad',
            field=models.CharField(max_length=150, verbose_name='Ürün adı'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='fiyat',
            field=models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Ürün fiyatı'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='kargo_ucreti',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Kargo ücreti'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.kategori', verbose_name='Ürün kategorisi'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='kayit_tarihi',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ürün kayıt tarihi'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='puan',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='Kullanıcı puanı'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='satici',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.magaza', verbose_name='Mağaza'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='satin_alanlar',
            field=models.ManyToManyField(blank=True, null=True, to='profiles.Kullanici', verbose_name='Bu ürünü satın alanlar'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='urun_resmi',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/urun_resimleri', verbose_name='Ürün resmi'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='urun_resmi_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Ürün resmi linki (tercihi)'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='baslik',
            field=models.CharField(max_length=50, verbose_name='Yorum başlığı'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='icerik',
            field=models.TextField(verbose_name='Yorum'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='puan',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Ürüne verilen puan'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='tarih',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yorum tarihi'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='yorum_yapan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.kullanici', verbose_name='Yorum sahibi'),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='yorum_yapilan_urun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.urun', verbose_name='Yorum yapılan ürün'),
        ),
        migrations.CreateModel(
            name='Bildirim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100, verbose_name='Başlık')),
                ('mesaj', models.TextField(verbose_name='Mesaj')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('kimden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.magaza', verbose_name='Kimden')),
                ('kime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.kullanici', verbose_name='Kime')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.urun')),
            ],
        ),
        migrations.AddField(
            model_name='magaza',
            name='kargolandi_bildirimi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.bildirim', verbose_name='Ürün kargolandı bildirimi.'),
        ),
    ]
