from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def prices(request):
    return HttpResponse('<h1>book prices--> from $1.2 to $11.4<h1><hr/>')


def shop_name(request):
    return HttpResponse('<h1>Shop name-->Central bookstore<h1><hr/>')