from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def shop_info(request):
    return HttpResponse('<h1>Shop products--> Books<h1><hr/>')


def product_types(request):
    return HttpResponse('<h1>Book types--> Novel, book-series, stories...<h1><hr/>')