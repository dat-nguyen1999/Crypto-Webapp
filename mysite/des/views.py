from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
import json
from . import DES
from .forms import UploadFileForm
from django.utils.http import urlquote
import gc
# Create your views here.


def des(request):
    return render(request,'des/des.html')

def DES_Encryption(request):
    if request.method == 'POST':
        fileInput = request.FILES['fileInput']
        filekey = request.FILES['filekey']
        #fileIV = request.FILES['ivencryptfile']

        mode = request.POST.get('dropdown')
        
        key = handle_uploaded_file(filekey)
        if len(key) != 8:
            return HttpResponse("Length of secret key should be 8 bytes key size!!!")
        if mode != "ECB":
            fileIV = request.FILES['ivencryptfile']
            IV = handle_uploaded_file(fileIV)
            if len(IV) != 8:
                return HttpResponse("Length of IV should be 8 bytes key size!!!")
        else:
            IV = None
        plaintext = handle_uploaded_file(fileInput)

        ciphertext = DES._DES_Encryption(key,plaintext,mode,IV)
        #print(key)
    
    response  = HttpResponse(ciphertext)
    #response['Content-Disposition'] = 'attachment; filename="dat.txt"'
    x = 'attachment; filename={}'.format("DES_Encrypted_Mode_" + mode + "_" + fileInput.name)
    #print(x)
    response['Content-Disposition'] = 'attachment; filename={}'.format("DES_Encrypted_Mode_" + mode + "_" + urlquote(fileInput.name))
    gc.collect()
    return response
    #return render(request,'des/des.html', {'ciphertex': ciphertext})
    

def DES_DEcryption(request):

    if request.method == 'POST':
        fileInput = request.FILES['de_fileInput']
        filekey = request.FILES['de_filekey']
        #fileIV = request.FILES['ivdecryptfile']

        mode = request.POST.get('de_dropdown')
        
        key = handle_uploaded_file(filekey)

        if len(key) != 8:
            return HttpResponse("Length of secret key should be 8 bytes key size!!!")
        if mode != "ECB":
            fileIV = request.FILES['ivdecryptfile']
            IV = handle_uploaded_file(fileIV)
            if len(IV) != 8:
                return HttpResponse("Length of IV should be 8 bytes key size!!!")
        else:
            IV = None
        
        ciphertext = handle_uploaded_file(fileInput)
        plaintext = DES._DES_Decryption(key,ciphertext,mode,IV)
        #print(key)
    
    response  = HttpResponse(plaintext)
    #response['Content-Disposition'] = 'attachment; filename="dat.txt"'

    response['Content-Disposition'] = 'attachment; filename={}'.format("DES_Decrypted_" + urlquote(fileInput.name))
    gc.collect()
    return response
    #return render(request,'des/des.html', {'ciphertex': ciphertext})


def handle_uploaded_file(f):
    output = b''
    # for chunk in f.chunks():
    #     output += chunk
    # return output
    while True:
        buf = f.read()
        if buf: 
            output += buf
        else:
            break
    return output