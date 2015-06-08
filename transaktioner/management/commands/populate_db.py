from django.core.management.base import BaseCommand
from transaktioner.models import Transaktion, Kategori, Sokord
from django.utils import timezone
import glob

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _importera_csv(self, csv):
        # importera csv
        # eller kanske från Excelfil direkt!


    def _lagg_in_transaktioner(self):

        #test = True




        if test:
            reskontradatum = timezone.now()
            transaktionsdatum = timezone.now()
            text = "Hahahaha"
            belopp = -46.4
            kommentar = "Hahahahah"

        q = Transaktion(
                reskontradatum = reskontradatum,
                transaktionsdatum = transaktionsdatum,
                text = text,
                belopp = belopp,
                kommentar = kommentar
        )

        q.save()

    def handle(self, *args, **options):
        self._lagg_in_transaktioner()
