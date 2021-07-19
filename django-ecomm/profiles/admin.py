from django.contrib import admin
from .models import Kullanici, Urun, Magaza, Kategori, Yorum, Bildirim, Siparis

admin.site.register(Kullanici)
admin.site.register(Magaza)
admin.site.register(Urun)
admin.site.register(Kategori)
admin.site.register(Yorum)
admin.site.register(Bildirim)
admin.site.register(Siparis)
