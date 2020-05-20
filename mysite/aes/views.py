from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
import json
from . import AES
import gc
from django.utils.http import urlquote


# Create your views here.
def aes(request):
    return render(request,'aes/aes.html')
def AES_Encryption(request):
    if request.method == 'POST':
        fileInput = request.FILES['fileInput']
        filekey = request.FILES['filekey']
        #fileIV = request.FILES['ivencryptfile']

        key_mode = request.POST.get('key_mode_en')
        
        mode = request.POST.get('dropdown')
        
        key = handle_uploaded_file(filekey)

        if key_mode == "Op1":
            if len(key) != 16:
                context = {
                    'reason': 'Length of secret key should be 16 bytes key size!!!'
                }
                gc.collect()
                return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        elif key_mode == "Op2":
            if len(key) != 24:
                context = {
                    'reason': 'Length of secret key should be 24 bytes key size!!!'
                }
                gc.collect()
                return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        elif key_mode == "Op3":
            if len(key) != 32:
                context = {
                    'reason': 'Length of secret key should be 32 bytes key size!!!'
                }
                gc.collect()
                return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        
        
        if mode == "ECB":
            IV = None
        else:
            fileIV = request.FILES['ivencryptfile']
            IV = handle_uploaded_file(fileIV)
            
            if mode in ["CBC", "CFB", "OFB"]:
                if len(IV) != 16:
                    context = {
                    }
                    gc.collect()
                    return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
            elif mode == "EAX":          
                if len(IV) > 16:
                    context = {
                        'reason': 'For ' + mode + ': Length of nonce must be 16 bytes!!!'
                    }
                    gc.collect()
                    return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
            else:
                pass
        plaintext = handle_uploaded_file(fileInput)

        ciphertext = AES._AES_Encryption(key,plaintext,mode,IV)
        if not isinstance(ciphertext, bytes):
            context = {
                    'reason': ciphertext.split("Caught this error: ")
                }
            gc.collect()
            return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
            
        #print(ciphertext)
        #print(len(ciphertext))
    
    response  = HttpResponse(ciphertext)
    #response['Content-Disposition'] = 'attachment; filename="dat.txt"'
    #x = 'attachment; filename={}'.format("TDES_Encrypted_Mode_" + mode + "_" + fileInput.name)
    #print(x)
    response['Content-Disposition'] = 'attachment; filename={}'.format("AES_Encrypted_Mode_" + mode + "_" + str(len(key)) + "_" + urlquote(fileInput.name))
    gc.collect()
    return response
    #return render(request,'des/des.html', {'ciphertex': ciphertext})



def AES_Decryption(request):
    if request.method == 'POST':
        fileInput = request.FILES['de_fileInput']
        filekey = request.FILES['de_filekey']
        #fileIV = request.FILES['ivdecryptfile']

        mode = request.POST.get('de_dropdown')

        key_mode = request.POST.get('key_mode_de')
        
        key = handle_uploaded_file(filekey)

        if key_mode == "Op1":
            if len(key) != 16:
                context = {
                    'reason': 'Length of secret key should be 16 bytes key size!!!'
                }
                return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        elif key_mode == "Op2":
            if len(key) != 24:
                context = {
                    'reason': 'Length of secret key should be 24 bytes key size!!!'
                }
                return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        elif key_mode == "Op3":
            if len(key) != 32:
                context = {
                    'reason': 'Length of secret key should be 32 bytes key size!!!'
                }
                return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        
        if mode == "ECB":
            IV = None
        else:
            fileIV = request.FILES['ivdecryptfile']
            IV = handle_uploaded_file(fileIV)
            
            if mode in ["CBC", "CFB", "OFB"]:
                if len(IV) != 16:
                    context = {
                        'reason': 'For ' + mode + ': Length of IV should be 16 bytes !!!'
                    }
                    gc.collect()
                    return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
            elif mode == "EAX":          
                if len(IV) > 16:
                    context = {
                        'reason': 'For ' + mode + ': Length of nonce must be 16 bytes!!!'
                    }
                    gc.collect()
                    return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
            else:
                pass
        
        ciphertext = handle_uploaded_file(fileInput)
        print(len(ciphertext))

        plaintext = AES._AES_Decryption(key,ciphertext,mode,IV)
        if not isinstance(plaintext, bytes):
            context = {
                    'reason': plaintext.split("Caught this error: ")
                }
            return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        #print(key)
    
    response  = HttpResponse(plaintext)
    #response['Content-Disposition'] = 'attachment; filename="dat.txt"'

    response['Content-Disposition'] = 'attachment; filename={}'.format("AES_Decrypted_" + urlquote(fileInput.name))
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