from django.shortcuts import render
from .models import Transaktion
from django.db.models import Sum
from datetime import datetime, timedelta
from django.views import generic
from .forms import DatumForm
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'transaktioner/last_month.html'
    context_object_name = 'last_month_list'
    objekt = Transaktion.objects

    def get_queryset(self):
        try:
            antal_dagar = int(self.request.GET.get('dagar'))
        except:
            antal_dagar = 30

        try:
            startdatum = self.request.GET.get('startdatum')
        except:
            startdatum = None

        if startdatum != None and startdatum != '':
            first_date = startdatum
        else:
            first_date = datetime.today() - timedelta(days=antal_dagar)

        return self.objekt.filter(transaktionsdatum__gte=first_date).order_by('-transaktionsdatum')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        summa = self.get_queryset().aggregate(Sum('belopp'))['belopp__sum']
        context['summa'] = summa
        return context

class KategoriView(IndexView):
#    first_date = datetime.today() - timedelta(days=30)
    
    def get_queryset(self):
        try:
            antal_dagar = int(self.request.GET.get('dagar'))
        except:
            antal_dagar = 30

        try:
            startdatum = self.request.GET.get('startdatum')
        except:
            startdatum = None

        if startdatum != None and startdatum != '':
            first_date = startdatum
        else:
            first_date = datetime.today() - timedelta(days=antal_dagar)


        query = self.objekt.filter(
                Q(transaktionsdatum__gte=first_date) & 
                Q(kategori__namn=self.kwargs['kategori'])).order_by('-transaktionsdatum')

        return query

#    def get_context_data(self, **kwargs):
#        context = super(IndexView, self).get_context_data(**kwargs)
#
#        summa = self.get_queryset().aggregate(Sum('belopp'))['belopp__sum']
#        context['summa'] = summa
#        return context

def last_month(request):
    last_month = datetime.today() - timedelta(days=30)
    last_month_list = Transaktion.objects.filter(transaktionsdatum__gte=last_month).order_by('-transaktionsdatum')
    #last_month_list = Transaktion.objects.all()

    context = {'last_month_list': last_month_list}
    return render(request, 'transaktioner/last_month.html', context)

def only_mat(request):
    last_month = datetime.today() - timedelta(days=30)
    last_month_list = Transaktion.objects.filter(transaktionsdatum__gte=last_month).filter(kategori__namn='Mat').order_by('-transaktionsdatum')
    summa = last_month_list.aggregate(Sum('belopp'))['belopp__sum']

    context = {'last_month_list': last_month_list, 'summa': summa}
    return render(request, 'transaktioner/last_month.html', context)
