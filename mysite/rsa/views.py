from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
import json
from . import RSA
from django.utils.http import urlquote
import gc
from io import BytesIO
from zipfile import ZipFile
# Create your views here.


def rsa(request):
    return render(request,'rsa/rsa.html')

def generateKey(request):
    
    if request.method == 'POST':
        key_length = int(request.POST['dropdown'])
        d_key = RSA.generateKeyPair(key_length)
        
        in_memory = BytesIO()
        zip = ZipFile(in_memory, "a")
            
        zip.writestr("publickey.txt", d_key['publickey'])
        zip.writestr("privatekey.txt", d_key['privatekey'])
        
        # fix for Linux zip files read in Windows
        for file in zip.filelist:
            file.create_system = 0    
            
        zip.close()

        in_memory.seek(0) 
        response = HttpResponse()
        #'attachment; filename={}'.format("keypair_" + str(key_length) + "bits_" + "rsa.zip")
        response["Content-Disposition"] = 'attachment; filename={}'.format("keypair_" + str(key_length) + "bits_" + "rsa.zip")
        response.write(in_memory.read())
        
        return response

def encrypt(request):
    if request.method == 'POST':
        fileInput = request.FILES['en_fileInput']
        filekey = request.FILES['en_keyfile']
        #fileIV = request.FILES['ivencryptfile']

        #key_mode = request.POST.get('dropdown')
                
        key = handle_uploaded_file(filekey)

        plt = handle_uploaded_file(fileInput)

        print(len(plt))
        if len(plt) > 245:
            context = {
                    'reason': "The length of file must be less than 245 bytes!!"
                }
            return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')

        ciphertxt = RSA.encrypt(key, plt)

        if not isinstance(ciphertxt,bytes):
            context = {
                    'reason': ciphertxt.split("Caught this error: ")
                }
            return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        
        response  = HttpResponse(ciphertxt)
        #response['Content-Disposition'] = 'attachment; filename="dat.txt"'

        response['Content-Disposition'] = "attachment; filename={}".format("RSA_Encrypted_" + urlquote(fileInput.name))
        return response

def decrypt(request):
    if request.method == 'POST':
        fileInput = request.FILES['de_fileInput']
        filekey = request.FILES['de_keyfile']
        #fileIV = request.FILES['ivencryptfile']

        #key_mode = request.POST.get('dropdown')
                
        key = handle_uploaded_file(filekey)

        cpt = handle_uploaded_file(fileInput)
        print(len(cpt))
        if len(cpt) > 256:
            context = {
                    'reason': "The length of file must be less than 245 bytes!!"
                }
            return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        
        plaintext = RSA.decrypt(key, cpt)

        if not isinstance(plaintext,bytes):
            context = {
                    'reason': plaintext.split("Caught this error: ")
                }
            return HttpResponse(json.dumps(context) ,status = 400, content_type='application/json')
        
        response  = HttpResponse(plaintext)
        #response['Content-Disposition'] = 'attachment; filename="dat.txt"'

        response['Content-Disposition'] = "attachment; filename={}".format("RSA_Decrypted_" + urlquote(fileInput.name))
        return response

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