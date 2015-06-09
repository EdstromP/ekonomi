# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from transaktioner.models import Transaktion, Kategori, Sokord
from django.utils import timezone
from django.db.models import Q
import glob
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'
    reskontradatum = transaktionsdatum = text = belopp = filnamn = None

    def add_arguments(self, parser):
        parser.add_argument('--xls', nargs='*')

    def _cell_text(self, cell):
        return " ".join(cell.stripped_strings)#.encode('utf-8')

    def _importera_xls(self, xls):
        global reskontradatum, transaktionsdatum, text, belopp, filnamn
    
        print("Öppnar %s" % xls)
        self.radnr = 1

        try:
            f = open(xls, mode='r', encoding='iso-8859-1')
            soup = BeautifulSoup(f)
        except IOError:
            print("Filnamn %s existerar inte." % xls)
            return

        for table in soup.find_all('table')[3:]:
            for row in table.find_all('tr'):
                columns = row.find_all(re.compile('t[dh]'))
                cols = [columns[0]] + [columns[2]] + [columns[4]] + [columns[6]]
                col = map(self._cell_text, cols)
                #print(list(col)[2])

                rad = list(col)

                reskontradatum = rad[0]
                transaktionsdatum = rad[1]
                text = rad[2]
                belopp = rad[3].replace(',','.').replace(' ','')

                # Fixa tomt reskontradatum till None
                if reskontradatum == '':
                    reskontradatum = None

                if reskontradatum != 'Reskontradatum':
                    filnamn = xls.split('/')[-1]
                    self._lagg_in_transaktioner()

                self.radnr += 1



    def _lagg_in_transaktioner(self):

        global reskontradatum, transaktionsdatum, text, belopp, filnamn

        #test = True

        print('%s;%s;%s;%s' % ( reskontradatum, transaktionsdatum, text, belopp ) )

#        if test:
#            reskontradatum = timezone.now()
#            transaktionsdatum = timezone.now()
#            text = "Hahahaha"
#            belopp = -46.4
#            kommentar = "Hahahahah"

        kommentar = ''
        kalla = filnamn
        importdatum = timezone.now().strftime('%Y-%m-%d')

        # Kolla om raden redan finns, i så fall ignorera
        if Transaktion.objects.filter(
                Q(reskontradatum = reskontradatum) &
                Q(transaktionsdatum = transaktionsdatum) &
                Q(text = text) &
                Q(belopp = belopp) &
                Q(kalla = kalla) &
                Q(radnr = self.radnr)).count() > 0:

            print("Rad finns redan. Ignorerar")
            self.ignorerade += 1
            return

        q = Transaktion(
                reskontradatum = reskontradatum,
                transaktionsdatum = transaktionsdatum,
                text = text,
                belopp = belopp,
                kommentar = kommentar,
                kalla = kalla,
                radnr = self.radnr,
                importdatum = importdatum
        )
        
        q.save()
        self.importerade += 1

    def handle(self, *args, **options):
        #self._lagg_in_transaktioner()
        
        self.importerade = 0
        self.ignorerade = 0

        if options['xls'] == None:
            print("Du måste ange --xls och filnamn")
            return

        for xls in options['xls']:
            self._importera_xls(xls)

        print(" ")
        print("Total importerades %d rader och %d ignorerades." % (self.importerade, self.ignorerade))

        #print('\"%s\"' % transaktionsdatum)

