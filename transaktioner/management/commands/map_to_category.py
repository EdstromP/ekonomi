from django.core.management.base import BaseCommand
from transaktioner.models import Transaktion, Kategori, Sokord
import time

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'test'

    def handle(self, *args, **options):

        start_time = time.time()

        transaktion_set = Transaktion.objects.all()
        sokord_set = Sokord.objects.all()

        for transaktion in transaktion_set.iterator():
            text = transaktion.text

            for sokord in sokord_set.iterator():
                #print("Sökord: %s; Text = %s" % (sokord.sokord, transaktion.text))
                if sokord.sokord in transaktion.text:
                    transaktion.kategori = sokord.kategori
                    transaktion.save()
                    break

        print("--- %s sekunder ---" % (time.time() - start_time))


