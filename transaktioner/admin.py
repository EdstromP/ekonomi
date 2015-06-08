from django.contrib import admin

from .models import Transaktion, Kategori, Sokord

admin.site.register(Transaktion)
admin.site.register(Kategori)
admin.site.register(Sokord)
