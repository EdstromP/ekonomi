from django.contrib import admin

from .models import Transaktion, Kategori, Underkategori, Sokord


class TransaktionAdmin(admin.ModelAdmin):
    list_display = ('transaktionsdatum','reskontradatum', 
            'text', 'belopp', 'kategori', 'underkategori', 'kommentar')

    list_filter = ('kategori',)

class SokordAdmin(admin.ModelAdmin):
    list_display = ('sokord', 'kategori', 'underkategori')

admin.site.register(Transaktion, TransaktionAdmin)
admin.site.register(Kategori)
admin.site.register(Underkategori)
admin.site.register(Sokord, SokordAdmin)
