from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def des(request):
    return render(request,'des/des.html')