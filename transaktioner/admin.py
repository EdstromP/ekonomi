from django.contrib import admin

from .models import Transaktion, Kategori, Sokord


class TransaktionAdmin(admin.ModelAdmin):
    list_display = ('reskontradatum', 'transaktionsdatum',
            'text', 'belopp', 'kommentar')

admin.site.register(Transaktion, TransaktionAdmin)
admin.site.register(Kategori)
admin.site.register(Sokord)
