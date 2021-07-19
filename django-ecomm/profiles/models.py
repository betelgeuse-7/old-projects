from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

from django.db.models.signals import pre_save
from django.dispatch import receiver

from profiles.slugify.app import slugify

class Kullanici(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Kullanıcı")
    slug = models.CharField(max_length=150, blank=True, verbose_name="Slug")
    profil_fotografi = models.ImageField(
        upload_to="profiles/kullanici_profil_fotograflari", null=True, blank=True, verbose_name="Profil fotoğrafı")
    toplam_harcanan_para = models.DecimalField(
        max_digits=999, decimal_places=2, default=0, verbose_name="Toplam harcanan para")
    kayit_tarihi = models.DateTimeField(
        auto_now_add=True, verbose_name="Kayıt tarihi")
    sepet = models.ManyToManyField(
        "Urun", blank=True, verbose_name="Sepet", related_name='sepet')
    satin_alinanlar = models.ManyToManyField(
        "Urun", blank=True, verbose_name="Satın alınan ürünler", related_name="satin_alinanlar")

    def __str__(self):
        return 'Kullanıcı: {}'.format(self.user.username)

    def get_username(self):
        return self.user.username

    def get_sepet(self):
        return self.sepet.all()

    def get_teslim_alinanlar(self):
        return self.teslim_alinanlar.all()

    def set_toplam_harcanan_para(self, fiyat, adet):
        self.toplam_harcanan_para = self.toplam_harcanan_para + fiyat * adet
        return super(Kullanici, self).save()


@receiver(pre_save, sender=Kullanici)
def make_kullanici_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username)


class Magaza(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=1)
    slug = models.CharField(max_length=100, verbose_name="Slug", blank=True)
    giris_adi = models.CharField(
        max_length=100, verbose_name="Ad", unique=True)
    gorunen_ad = models.CharField(
        max_length=100, verbose_name='Mağazanın adı', unique=True)
    profil_fotografi = models.ImageField(
        upload_to="profiles/magaza_profil_fotograflari", null=True, blank=True, verbose_name="Fotoğraf")
    tanitim = models.TextField(verbose_name="Mağaza tanıtım yazısı")
    bekleyen_para = models.DecimalField(
        decimal_places=2, max_digits=999, verbose_name="Askıdaki para", default=0)
    brut_kazanc = models.DecimalField(
        max_digits=999, decimal_places=2, verbose_name="Brüt kazanç (Site komisyonu hariç)", default=0)
    net_kazanc = models.DecimalField(
        max_digits=999, decimal_places=2, verbose_name="Net kazanç", default=0)
    ortalama_puan = models.DecimalField(
        max_digits=2, decimal_places=1, default=0.0, verbose_name="Ortalama puan")
    kayit_tarihi = models.DateTimeField(
        auto_now_add=True, verbose_name="Kayıt tarihi")

    def __str__(self):
        return 'Mağaza: {}'.format(self.gorunen_ad)

@receiver(pre_save, sender=Magaza)
def make_magaza_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.gorunen_ad)




class Urun(models.Model):
    ad = models.CharField(max_length=150, verbose_name="Ürün adı")
    slug = models.CharField(max_length=150, verbose_name="Slug", blank=True)
    satici = models.ForeignKey(
        Magaza, on_delete=models.CASCADE, verbose_name="Mağaza")
    aciklama = models.TextField(verbose_name="Ürün açıklaması")
    urun_resmi = models.ImageField(
        upload_to='profiles/urun_resimleri', blank=True, null=True, verbose_name="Ürün resmi")
    urun_resmi_url = models.URLField(
        max_length=300, blank=True, null=True, verbose_name="Ürün resmi linki (tercihi)")
    fiyat = models.DecimalField(
        max_digits=999, decimal_places=2, verbose_name="Ürün fiyatı")
    kategori = models.ForeignKey(
        "Kategori", on_delete=models.CASCADE, verbose_name="Ürün kategorisi")
    kargo_ucreti = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name="Kargo ücreti")
    kime_kargolandi = models.ManyToManyField(
        Kullanici, blank=True, verbose_name='Şu kişilere kargolandı.', related_name='kime_kargolandi')
    puan = models.DecimalField(
        max_digits=2, decimal_places=1, default=0.0, verbose_name="Kullanıcı puanı")
    satin_alanlar = models.ManyToManyField(
        Kullanici, blank=True, verbose_name="Bu ürünü satın alanlar", related_name='satin_alanlar')
    kayit_tarihi = models.DateTimeField(
        auto_now_add=True, verbose_name="Ürün kayıt tarihi")

    def __str__(self):
        return 'Ürün: {}'.format(self.ad)

    def get_kime_kargolandi(self):
        return self.kime_kargolandi.all()

    def get_satin_alanlar(self):
        return self.satin_alanlar.all()

    def get_urun_resmi(self):
        if self.urun_resmi and hasattr(self.urun_resmi, 'url'):
            return self.urun_resmi.url


@receiver(pre_save, sender=Urun)
def make_urun_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.ad)


def get_kategori_urunleri(id):
    kategori = Kategori.objects.get(id=id)
    urunler = Urun.objects.filter(kategori=kategori).all()
    return urunler


class Kategori(models.Model):
    ad = models.CharField(max_length=100, verbose_name="Kategori adı")
    slug = models.CharField(max_length=150, verbose_name="Slug", blank=True)

    def __str__(self):
        return 'Kategori: {}'.format(self.ad)


@receiver(pre_save, sender=Kategori)
def make_kategori_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.ad)


class Yorum(models.Model):
    yorum_yapan = models.ForeignKey(
        Kullanici, on_delete=models.CASCADE, verbose_name="Yorum sahibi")
    yorum_yapilan_urun = models.ForeignKey(
        Urun, on_delete=models.CASCADE, verbose_name="Yorum yapılan ürün")
    tarih = models.DateTimeField(
        auto_now_add=True, verbose_name="Yorum tarihi")
    baslik = models.CharField(max_length=50, verbose_name="Yorum başlığı")
    icerik = models.TextField(verbose_name="Yorum")
    puan = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Ürüne verilen puan")

    def __str__(self):
        return "'{}' kullanıcısı tarafından '{}' ürününe yapıldı.".format(self.yorum_yapan.user.username, self.yorum_yapilan_urun.ad)


class Bildirim(models.Model):
    kimden = models.ForeignKey(
        Magaza, on_delete=models.CASCADE, verbose_name='Kimden')
    kime = models.ManyToManyField(
        Kullanici, verbose_name='Kime')
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    mesaj = models.TextField(verbose_name='Mesaj')
    tarih = models.DateTimeField(auto_now_add=True)
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kimden}'den {self.kime.all()[0]}... kullanıcılarına..."


class Siparis(models.Model):
    satin_alan = models.ForeignKey(
        Kullanici, on_delete=models.CASCADE, verbose_name="Satın alan")
    satin_alan_ad = models.CharField(
        max_length=100, verbose_name="Satın alan adı")
    satin_alan_soyad = models.CharField(
        max_length=100, verbose_name="Satın alan soyadı")
    tel_no = models.CharField(max_length=13, verbose_name="Telefon numarası")
    adres = models.CharField(max_length=150, verbose_name="Adres")
    kart_guvenlik_kodu = models.CharField(max_length=3, verbose_name="CVV/CVC")
    kart_skt = models.CharField(max_length=5, verbose_name="Kart SKT")
    satici = models.ForeignKey(
        Magaza, on_delete=models.CASCADE, verbose_name="Satıcı")
    urun = models.ForeignKey(
        Urun, on_delete=models.CASCADE, verbose_name="Ürün")
    adet = models.PositiveIntegerField(default=1, verbose_name="Adet")
    siparis_tarihi = models.DateTimeField(
        auto_now_add=True, verbose_name="Sipariş tarihi")
    kargoya_verilme_tarihi = models.DateTimeField(
        blank=True, null=True, verbose_name="Kargoya verilme tarihi")
    teslim_alinma_tarihi = models.DateTimeField(
        blank=True, null=True, verbose_name="Teslim alınma tarihi")
    tamamlandi = models.BooleanField(default=False, verbose_name="Tamamlandı")

    def __str__(self):
        return f"Sipariş: {self.urun.ad} --> {self.satin_alan_ad} {self.satin_alan_soyad} "

    # can't modify from views
    # I think it is editable=False
    def set_kargoya_verilme_tarihi(self):
        self.kargoya_verilme_tarihi = timezone.now()
        return super(Siparis, self).save()
    
    def set_teslim_alinma_tarihi(self):
        self.teslim_alinma_tarihi = timezone.now()
        return super(Siparis, self).save()

    def set_tamamlandi_true(self):
        self.tamamlandi = True
        return super(Siparis, self).save()

