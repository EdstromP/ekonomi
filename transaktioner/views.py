from django.shortcuts import render
from .models import Transaktion
from django.db.models import Sum
from datetime import datetime, timedelta

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
