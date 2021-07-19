from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from . import models
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django import forms

from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponse, Http404, JsonResponse

import json

from django.utils import timezone


class IndexPage(View):
    def get(self, request):
        kategoriler = models.Kategori.objects.all()
        magazalar = models.Magaza.objects.all()[:10]
        urunler = models.Urun.objects.all()[:50]

        context = {
            'kategoriler': kategoriler,
            'magazalar': magazalar,
            'urunler': urunler
        }

        return render(request, 'html/index.html', context)


class UyeOl(View):
    def get(self, request):
        return render(request, 'html/uyeol.html')

    def post(self, request):
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        k_adi = request.POST.get('k-adi')
        e_mail = request.POST.get('e-mail')
        sifre = request.POST.get('sifre')
        sifre2 = request.POST.get('sifre2')
        p_fotografi = request.FILES.get('p-fotografi')

        all_emails = []
        users = User.objects.all()
        for u in users:
            all_emails.append(u.email)

        if e_mail in all_emails:
            raise forms.ValidationError(
                "Bu e-posta ile bir kullanıcı zaten var.")

        if len(k_adi) < 5:
            raise forms.ValidationError('Kullanıcı adı çok kısa.')
        if sifre != sifre2:
            raise forms.ValidationError('Şifreler uyuşmuyor.')

        user = User.objects.create(first_name=ad, last_name=soyad,
                                   username=k_adi, email=e_mail, password=sifre)
        user.set_password(sifre)
        user.save()

        if p_fotografi:
            models.Kullanici.objects.create(
                user=user, profil_fotografi=p_fotografi)
        else:
            models.Kullanici.objects.create(user=user)

        return redirect(reverse('profiles:index'))


class MagazaAc(View):
    def get(self, request):
        return render(request, 'html/magazaac.html')

    def post(self, request):
        magaza_adi = request.POST.get('ad')
        email = request.POST.get('email')
        sifre = request.POST.get('sifre')
        tanitim = request.POST.get('tanitim')
        m_foto = request.FILES.get('m-foto')

        if len(magaza_adi) < 8:
            raise forms.ValidationError('Ad çok kısa.')

        if '@' not in email:
            raise forms.ValidationError('Geçerli bir email adresi girin.')

        all_emails = []
        all_names = []
        magazaqs = models.Magaza.objects.all()
        usersqs = models.User.objects.all()
        for m in magazaqs:
            all_emails.append(m.user.email)
            all_names.append(m.gorunen_ad)
        for u in usersqs:
            all_emails.append(u.email)

        if email in all_emails:
            raise forms.ValidationError(
                "Bu e-posta adresi zaten kullanılıyor.")

        if magaza_adi in all_names:
            raise forms.ValidationError('Mağaza adları eşsiz olmalıdır.')

        if len(sifre) < 8:
            raise forms.ValidationError('Şifre çok kısa.')

        errors = []
        for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if n not in sifre:
                errors.append('E')
        if len(errors) == 10:
            raise forms.ValidationError('Şifre en az 1 rakam içermeli.')

        if not tanitim:
            raise forms.ValidationError('Tanıtım girin.')

        if m_foto:
            c_user = models.User.objects.create(
                email=email, password=make_password(sifre), username=email)
            c_user.save()

            magaza = models.Magaza.objects.create(
                user=c_user, profil_fotografi=m_foto, giris_adi=c_user.username, gorunen_ad=magaza_adi)
            magaza.save()

        else:
            c_user = models.User.objects.create(
                email=email, password=make_password(sifre), username=email)
            c_user.save()

            magaza = models.Magaza.objects.create(
                user=c_user, giris_adi=c_user.username, gorunen_ad=magaza_adi)
            magaza.save()

        return redirect('/')


class Giris(View):
    def get(self, request):
        return render(request, 'html/giris.html')

    def post(self, request):
        k_adi = request.POST.get('k-adi')
        sifre = request.POST.get('sifre')

        user = authenticate(username=k_adi, password=sifre)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return redirect(reverse('profiles:giris'))


class MagazaGiris(View):
    def get(self, request):
        return render(request, 'html/magaza_giris.html')

    def post(self, request):
        try:
            email = request.POST.get('email')
            sifre = request.POST.get('sifre')

            pwd_to_auth = User.objects.get(email=email).password

            pwd_check = check_password(sifre, pwd_to_auth)

            if pwd_check:
                user = authenticate(username=email, password=sifre)

                if user:
                    login(request, user)
                    return redirect('/')
                else:
                    return redirect('profiles:magaza-giris')
            else:
                return render(request, 'html/hata.html', {
                    "hata": "Giriş bilgileri hatalı."
                })
        except:
            return render(request, 'html/hata.html', {
                "hata": "Giriş bilgileri hatalı."
            })


class Cikis(View):
    def get(self, request):
        logout(request)
        return redirect('/')


def urun_detay(request, slug):
    try:
        urun = models.Urun.objects.get(slug=slug)
        current_kullanici = models.Kullanici.objects.get(id=request.user.id)
        current_user_sepet = current_kullanici.sepet.all()

        user_has_yorum = True

        yorumlar = models.Yorum.objects.filter(yorum_yapilan_urun=urun).all().order_by('-tarih')
        yorum_authors = []

        for yorum in yorumlar:
            yorum_authors.append(yorum.yorum_yapan)

        if not current_kullanici in yorum_authors:
            user_has_yorum = False
        

        context = {
                    "urun": urun,
                   "magazanin_diger_urunleri": models.Urun.objects.filter(satici=urun.satici).exclude(slug=slug)[:10],
                   "user_sepet": current_user_sepet,
                   "yorumlar": yorumlar,
                   "user_has_yorum":user_has_yorum,
                   }
        return render(request, "html/urun_detay.html", context)
    except:
        urun = models.Urun.objects.get(slug=slug)
        context = {"urun": urun,
                   "magazanin_diger_urunleri": models.Urun.objects.filter(satici=urun.satici).exclude(slug=slug)[:10],
                   "yorumlar": models.Yorum.objects.filter(yorum_yapilan_urun=urun).all().order_by('-tarih'),
                   }
        return render(request, "html/urun_detay.html", context)


class YeniUrun(View):
    def get(self, request):
        context = {"kategoriler": models.Kategori.objects.all()}
        return render(request, 'html/yeni_urun.html', context)

    def post(self, request):
        # data from the html form
        ad = request.POST.get("ad")
        aciklama = request.POST.get("aciklama")
        resim = request.FILES.get("resim")
        fiyat = request.POST.get("fiyat")
        kategori_ad = request.POST.get("kategoriler").strip()
        k_ucreti = request.POST.get("k_ucreti")

        # the rest
        try:
            satici = models.Magaza.objects.get(giris_adi=request.user.email)
        except:
            raise forms.ValidationError("Bu bir mağaza değil.")
        kategori = models.Kategori.objects.get(ad=kategori_ad)

        if ad or aciklama or resim or fiyat or kategori or k_ucreti != '' or ' ':
            if satici:
                try:
                    urun = models.Urun.objects.create(ad=ad,
                                                      satici=satici,
                                                      aciklama=aciklama,
                                                      urun_resmi=resim,
                                                      fiyat=fiyat,
                                                      kategori=kategori,
                                                      kargo_ucreti=k_ucreti,
                                                      )
                    urun.save()

                    return redirect("/")
                except:
                    raise forms.ValidationError("Bir şeyler yanlış gitti.")
        else:
            raise forms.ValidationError("Hatalı girdi.")


class KategoriUrunleri(View):
    def get(self, request, slug):
        try:
            kategori = models.Kategori.objects.get(slug=slug)
            if kategori:
                try:
                    kategori_urunleri = models.Urun.objects.filter(
                        kategori=kategori)
                    return render(request, 'html/kategori_urunleri.html', {
                        "urunler": kategori_urunleri,
                        "k_adi": kategori.ad
                    })
                except:
                    return render(request, 'html/kategori_urunleri.html')

            else:
                raise Http404
        except:
            raise Http404


class SepeteEkle(View):
    def get(self, request, id):
        return HttpResponse("NO GET.")

    def post(self, request, id):
        urunid = id
        try:
            userid = json.loads(request.body)['user']
            user = models.Kullanici.objects.get(id=userid)
            if user:
                user.sepet.add(urunid)
            else:
                return JsonResponse({"msg": "No user with this ID."})

            return JsonResponse({"msg": "Ürün sepetinize eklendi."})

        except:
            print("ERROR")
            return JsonResponse({"msg": "Sadece normal kullanıcılar."})


class SepetiGoruntule(View):
    def get(self, request, slug):
        try:
            user = models.Kullanici.objects.get(slug=slug)
            req_user_slug = models.Kullanici.objects.get(
                id=request.user.id).slug
            if user:
                if request.user.id == user.id:
                    sepet_urunleri = user.sepet.all()
                    context = {
                        "sepetteki_urunler": sepet_urunleri,
                    }
                    return render(request, 'html/sepet.html', context)
                else:
                    return redirect(reverse("profiles:sepet", args=(req_user_slug, )))
            else:
                raise Http404
        except:
            raise Http404


class HesabiGoruntule(View):
    def get(self, request, slug):
        try:
            kullanici = models.Kullanici.objects.get(slug=slug)
            if kullanici:
                user_slug = kullanici.slug
                if request.user.id == kullanici.id:

                    satin_aldiklari = kullanici.satin_alinanlar.all()
                    siparisler = models.Siparis.objects.filter(satin_alan=kullanici).all()

                    context = {
                        "kullanici": kullanici,
                        "satin_aldiklari": satin_aldiklari,
                        "siparisler":siparisler,
                    }
                    return render(request, 'html/hesap.html', context)
                else:
                    return redirect(reverse('profiles:sepet', args=(user_slug, )))
            else:
                raise Http404
        except:
            raise Http404


class Siparis(View):
    def get(self, request, slug):
        try:
            urun = models.Urun.objects.get(slug=slug)
            return render(request, 'html/siparis_form.html',
                          {
                              "urun": urun
                          })
        except:
            raise Http404


class UrunSiparisEt(View):
    def post(self, request, id):
        try:
            userid = request.user.id

            if userid:

                try:
                    urun = models.Urun.objects.get(id=id)
                    kullanici = models.Kullanici.objects.get(id=userid)
                    satici = urun.satici

                    try:
                        kullanici.sepet.remove(urun)
                        kullanici.satin_alinanlar.add(urun)

                        satici.bekleyen_para += urun.fiyat - (urun.fiyat / 10)
                        satici.save()

                        adet = request.POST.get('adet')
                        ad = request.POST.get('ad')
                        soyad = request.POST.get('soyad')
                        tel = request.POST.get('tel')
                        adres = request.POST.get('adres')
                        kgk = request.POST.get('kgk')
                        skt1 = request.POST.get('skt1')
                        skt2 = request.POST.get('skt2')

                        skt = skt1 + '/' + skt2

                        try:
                            siparis = models.Siparis.objects.create(satin_alan=kullanici,
                                                                    satin_alan_ad=ad,
                                                                    satin_alan_soyad=soyad,
                                                                    tel_no=tel,
                                                                    adres=adres,
                                                                    kart_guvenlik_kodu=kgk,
                                                                    kart_skt=skt,
                                                                    satici=urun.satici,
                                                                    urun=urun,
                                                                    adet=adet)

                            siparis.save()

                            return render(request, 'html/siparis_alindi.html', {
                                "urun": urun
                            })

                        except:
                            return render(request, 'html/hata.html', {
                                "hata": "Sipariş oluşturulamadı."
                            })

                    except:
                        return render(request, 'html/hata.html', {
                            "hata": "Ürün bilgileri hatalı."
                        })

                except:
                    return render(request, 'html/hata.html', {
                        "hata": "Bilgiler hatalı."
                    })

        except:
            return render(request, 'html/hata.html')


class MagazamiGoruntule(View):
    def get(self, request):

        try:
            magaza = models.Magaza.objects.get(user=request.user)

            if magaza:
                urunler = []
                siparisler = []

                urunler_qs = models.Urun.objects.filter(satici=magaza)
                siparisler_qs = models.Siparis.objects.filter(satici=magaza)

                for urun in urunler_qs:
                    urunler.append(urun)

                for siparis in siparisler_qs:
                    siparisler.append(siparis)

                context = {
                    "magaza": magaza,
                    "urunler": urunler,
                    "siparisler": siparisler}
                return render(request, 'html/magazam.html', context)

        except:
            raise Http404


class Kargola(View):
    def post(self, request):
        try:
            siparisID = json.loads(request.body)['siparisID']

            try:
                siparis = models.Siparis.objects.get(id=siparisID)

                siparis.set_kargoya_verilme_tarihi()

                return JsonResponse(
                    {
                        "msg": "OK"
                    }
                )

            except:
                return render(request, 'html/hata.html', {
                    "hata": "Sipariş ve/veya satıcı bilgileri bulunamadı."
                })

        except:
            return render(request, 'html/hata.html', {
                "hata": "Bir hata oluştu."
            })


class TeslimAlindi(View):
    def post(self, request):
        try:
            urunid = json.loads(request.body)['urunID']
            saticiid = json.loads(request.body)['saticiID']
            siparisid = json.loads(request.body)['siparisID']
            adet = json.loads(request.body)['adet']

            if urunid and saticiid and siparisid and adet:
                try:
                    urun = models.Urun.objects.get(id=urunid)
                    kullanici = models.Kullanici.objects.get(user=request.user)
                    satici = models.Magaza.objects.get(id=saticiid)
                    siparis = models.Siparis.objects.get(id=siparisid)

                    if urun and kullanici and satici and siparis:
                        try:
                            #kullanici 
                            kullanici.toplam_harcanan_para += kullanici.toplam_harcanan_para + urun.fiyat
                            kullanici.satin_alinanlar.remove(urun)

                            kullanici.save()

                            #magaza
                            if not satici.bekleyen_para == 0:
                                satici.bekleyen_para -= urun.fiyat - (urun.fiyat / 10)

                            satici.brut_kazanc += urun.fiyat
                            satici.net_kazanc += urun.fiyat - (urun.fiyat / 10)

                            satici.save()

                            #siparis 
                            siparis.set_teslim_alinma_tarihi()
                            siparis.set_tamamlandi_true()

                            siparis.save()


                            return JsonResponse(
                                {
                                    "msg":"OK"
                                }
                            )

                        except:
                            return JsonResponse(
                                {
                                    "errmsg":"Bir hata oluştu."
                                }
                            )

                except:
                    return JsonResponse(
                        {
                            "errmsg":"Bilgiler hatalı"
                        }
                    )

        except:
            return JsonResponse(
                {
                    "errmsg":"Bilgiler alınamadı."
                }
            )

class Yorumla(View):
    def post(self, request, slug):
        try:
            user = request.user
            kullanici = models.Kullanici.objects.get(user=user)
            urun = models.Urun.objects.get(slug=slug)

            puan = request.POST.get('puan')
            baslik = request.POST.get('baslik')
            yorum = request.POST.get('yorum')

            urun_yorumlari = models.Yorum.objects.filter(yorum_yapilan_urun=urun).all()

            urun_yorumlari_authors = []

            for yorum in urun_yorumlari:
                urun_yorumlari_authors.append(yorum.yorum_yapan)

            if not kullanici in urun_yorumlari_authors:
                try:
                    yorum_obj = models.Yorum.objects.create(yorum_yapan=kullanici,
                                                        yorum_yapilan_urun=urun,
                                                        baslik=baslik,
                                                        icerik=yorum,
                                                        puan=puan)
                    yorum_obj.save()

                    return redirect(reverse('profiles:urun-detay', args=(urun.slug,)))

                except:
                    return render(request, 'html/hata.html', 
                    {
                        "hata":"Yorum oluşturulamadı."
                    })
            else:
                return render(request, "html/hata.html", {
                    "hata":"Bu ürüne zaten yorum yaptınız."
                })
        
        except:
            return render(request, "html/hata.html", {
                "hata": "Bilgiler alınamadı."
            })

class MagazaDetay(View):
    def get(self, request, slug):
        try:
            magaza = models.Magaza.objects.get(slug=slug)
            urunler = models.Urun.objects.filter(satici=magaza)
            context = {
                "magaza": magaza,
                "urunler": urunler,
            }
            return render(request, 'html/magaza_detay.html', context)
        except:
            raise Http404

class UrunAra(View):
    def post(self, request):
        query = request.POST.get("query")

        urunler = []
        urunler_qs = models.Urun.objects.filter(ad__icontains=query)

        for urun in urunler_qs:
            urunler.append(urun)

        context = {
            "urunler":urunler,
            "query":query
        }
        
        return render(request, 'html/urun_arama_sonuc.html', context)


