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
        fileIV = request.FILES['ivencryptfile']

        mode = request.POST.get('dropdown')
        
        key = handle_uploaded_file(filekey)
        if len(key) != 8:
            return HttpResponse("Length of secret key should be 8 bytes key size!!!")
        IV = handle_uploaded_file(fileIV)
        if len(key) != 8:
            return HttpResponse("Length of IV should be 8 bytes key size!!!")

        plaintext = handle_uploaded_file(fileInput)

        ciphertext = DES._DES_Encryption(key,plaintext,mode,IV)
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
        fileIV = request.FILES['ivdecryptfile']

        
        key = handle_uploaded_file(filekey)

        if len(key) != 8:
            return HttpResponse("Length of secret key should be 8 bytes key size!!!")
        IV = handle_uploaded_file(fileIV)
        if len(key) != 8:
            return HttpResponse("Length of IV should be 8 bytes key size!!!")
        
        mode = request.POST.get('de_dropdown')
        ciphertext = handle_uploaded_file(fileInput)
        plaintext = DES._DES_Decryption(key,ciphertext,mode,IV)
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