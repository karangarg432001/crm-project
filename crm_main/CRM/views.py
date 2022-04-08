from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#from .filters import Query1Filter


def dashboard(request):
    querys = Query1.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_queries = querys.count()
    pending = querys.filter(status='Pending').count()
    confirmed = querys.filter(status='Confirmed').count()
    progress = querys.filter(status='UNDER_PROGRESS').count()
    review = querys.filter(status='TEAM_REVIEWING').count()
    resolved = querys.filter(status='RESOLVED').count()

    context = {'query': querys, 'customers': customers, 'total_customers': total_customers,
               'total_queries': total_queries, 'pending': pending,
               'confirmed': confirmed, 'progress': progress, 'review': review, 'resolved': resolved}

    return render(request, 'CRM/dashboard.html', context)


def detail(request):
    detail = Detail.objects.all()

    return render(request, 'CRM/detail.html', {'detail': detail})


def customer(request):
    return render(request, 'CRM/customer.html')
