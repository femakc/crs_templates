# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'message/index.html'
    prod_name = 'CRS'
    context = {
        'template': template,
        'prod_name': prod_name,
    }
    return render(request, template, context)
