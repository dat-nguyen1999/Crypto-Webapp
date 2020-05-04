from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
import json
from . import DES
from .forms import UploadFileForm

# Create your views here.


def des(request):
    return render(request,'des/des.html')

def DES_Encryption(request):
    if request.method == 'POST':
        fileInput = request.FILES['fileInput']
        filekey = request.FILES['filekey']
       
        mode = request.POST.get('dropdown')
        key = handle_uploaded_file(filekey)
        plaintext = handle_uploaded_file(fileInput)
    
        ciphertext = DES._DES_Encryption(key,plaintext,mode)
        #print(key)
    
    response  = HttpResponse(ciphertext)
    #response['Content-Disposition'] = 'attachment; filename="dat.txt"'

    response['Content-Disposition'] = 'attachment; filename={}'.format("DES_Encrypted_"+fileInput.name)
    return response
    #return render(request,'des/des.html', {'ciphertex': ciphertext})

def DES_DEcryption(request):

    if request.method == 'POST':
        fileInput = request.FILES['de_fileInput']
        filekey = request.FILES['de_filekey']
       
        mode = request.POST.get('de_dropdown')
        key = handle_uploaded_file(filekey)
        ciphertext = handle_uploaded_file(fileInput)
    
        plaintext = DES._DES_Decryption(key,ciphertext,mode)
        #print(key)
    
    response  = HttpResponse(plaintext)
    #response['Content-Disposition'] = 'attachment; filename="dat.txt"'

    response['Content-Disposition'] = 'attachment; filename={}'.format("DES_Decrypted_"+fileInput.name)
    return response
    #return render(request,'des/des.html', {'ciphertex': ciphertext})


def handle_uploaded_file(f):
    output = b''
    for chunk in f.chunks():
        output += chunk
    return output