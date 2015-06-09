from django.shortcuts import render
from .models import Transaktion
from datetime import datetime, timedelta

def last_month(request):
    last_month = datetime.today() - timedelta(days=30)
    last_month_list = Transaktion.objects.filter(transaktionsdatum__gte=last_month).order_by('-transaktionsdatum')
    #last_month_list = Transaktion.objects.all()

    context = {'last_month_list': last_month_list}
    return render(request, 'transaktioner/last_month.html', context)

