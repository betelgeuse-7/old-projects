from django.urls import path
from . import views

from django.conf.urls.static import static, settings


app_name = "profiles"

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('uye-ol/', views.UyeOl.as_view(), name='uye-ol'),
    path('magaza/ac/', views.MagazaAc.as_view(), name='magaza-ac'),
    path('giris/', views.Giris.as_view(), name='giris'),
    path('giris/magaza/', views.MagazaGiris.as_view(), name='magaza-giris'),
    path('cikis/', views.Cikis.as_view(), name='cikis'),
    path('urun/<str:slug>/', views.urun_detay, name='urun-detay'),
    path('yeni-urun/', views.YeniUrun.as_view(), name='yeni-urun'),
    path('kategori/<str:slug>/', views.KategoriUrunleri.as_view(),
         name='kategori-urunleri'),
    path('sepete-ekle/<int:id>/',
         views.SepeteEkle.as_view(), name="sepete-ekle"),
    path('<str:slug>/sepet/', views.SepetiGoruntule.as_view(), name="sepet"),
    path('<str:slug>/hesap/', views.HesabiGoruntule.as_view(), name="hesap"),
    path('satin-al/<str:slug>/', views.Siparis.as_view(), name="siparis-form"),
    path('siparis-et/<int:id>/', views.UrunSiparisEt.as_view(), name="siparis"),
    path('magazam/', views.MagazamiGoruntule.as_view(), name="magazam"),
    path('kargola/', views.Kargola.as_view(), name="kargola"),
    path('teslim-al/', views.TeslimAlindi.as_view(), name="teslim"),
    path('yorumla/<str:slug>/', views.Yorumla.as_view(), name="yorumla"),
    path('magaza/<str:slug>/', views.MagazaDetay.as_view(), name="magaza-detay"),
    path('urun-ara/', views.UrunAra.as_view(), name="urun-ara"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
