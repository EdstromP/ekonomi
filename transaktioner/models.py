from django.db import models
from django.core.urlresolvers import reverse

class Transaktion(models.Model):
    reskontradatum = models.DateField(null=True)
    transaktionsdatum = models.DateField()
    text = models.CharField(max_length=50)
    belopp = models.FloatField()
    kommentar = models.TextField(max_length=500, blank=True)
    kategori = models.ForeignKey('Kategori', null=True)
    underkategori = models.ForeignKey('Underkategori', null=True, blank=True)
    kalla = models.CharField(max_length=100, blank=True)
    radnr = models.IntegerField(null=True)
    importdatum = models.DateField(null=True)

    def __str__(self):
        return '%s %f' % (self.text, self.belopp)

    def get_absolute_url(self):
        return reverse('transaktioner:uppdatera', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.kategori != None and self.kategori != '':
            obj, created = Sokord.objects.update_or_create(sokord=self.text, defaults={"kategori": self.kategori, "underkategori": self.underkategori})
            
            Transaktion.objects.all().filter(text=self.text).update(kategori=self.kategori, underkategori=self.underkategori)

        super(Transaktion, self).save(*args, **kwargs)

class Kategori(models.Model):
    namn = models.CharField(max_length=30, unique=True)
    kommentar = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return '%s' % self.namn

class Underkategori(models.Model):
    namn = models.CharField(max_length=30)
    kommentar = models.TextField(max_length=500, blank=True)
    kategori = models.ForeignKey('Kategori')

    def __str__(self):
        return '%s/%s' % (self.kategori, self.namn)

class Sokord(models.Model):
    sokord = models.CharField(max_length=20, unique=True)
    kategori = models.ForeignKey('Kategori')
    underkategori = models.ForeignKey('Underkategori', null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.sokord, self.kategori)
