from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
import json
#from . import DES
from django.utils.http import urlquote
import gc
# Create your views here.


def rsa(request):
    return render(request,'rsa/rsa.html')

