from django.db import models

class Transaktion(models.Model):
    reskontradatum = models.DateField(null=True)
    transaktionsdatum = models.DateField()
    text = models.CharField(max_length=50)
    belopp = models.FloatField()
    kommentar = models.TextField(max_length=500, blank=True)
    kategori = models.ForeignKey('Kategori', null=True)
    kalla = models.CharField(max_length=100, blank=True)
    radnr = models.IntegerField(null=True)
    importdatum = models.DateField(null=True)

    def __str__(self):
        return '%s %f' % (self.text, self.belopp)

class Kategori(models.Model):
    namn = models.CharField(max_length=30)
    kommentar = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return '%s' % self.namn

class Sokord(models.Model):
    sokord = models.CharField(max_length=20)
    kategori = models.ForeignKey('Kategori')

    def __str__(self):
        return '%s: %s' % (self.sokord, self.kategori)
