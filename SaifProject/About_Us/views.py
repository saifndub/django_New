from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_us(request):
    return HttpResponse('This is about us plarform.')