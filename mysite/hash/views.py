from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
import json
from Crypto.Random import get_random_bytes
from . import HASH
import gc

# Create your views here.
def hash(request):
    return render(request,'hash/hash.html')

def HASH_Encryption(request):
    if request.is_ajax():
        if(request.method == 'POST'):
            algorithm = request.POST['dropdown']
            originalfile = request.FILES['originalfile']
            outputfile = request.FILES['outputfile']

            key = b''
            original = handle_uploaded_file(originalfile)
            output = handle_uploaded_file(outputfile)

            jsrv = {
                'hash_value_ori': HASH._Hash_Encryption(original, key, algorithm),
                'hash_value_out': HASH._Hash_Encryption(output, key, algorithm)
            }
            gc.collect()
            return HttpResponse(json.dumps(jsrv),content_type='aplication/json')
        else:
            pass


    else:
        print("not ajax")
        if(request.method == 'POST'):
            algorithm = request.POST['dropdown']
            originalfile = request.FILES['originalfile']
            outputfile = request.FILES['outputfile']

            key = get_random_bytes(8)
            original = handle_uploaded_file(originalfile)
            output = handle_uploaded_file(outputfile)

            jsrv = {
                'hash_value_ori': HASH._Hash_Encryption(original, key, algorithm),
                'hash_value_out': HASH._Hash_Encryption(output, key, algorithm),
            }
            gc.collect()
            return HttpResponse(jsrv,content_type='aplication/json')
            #return jsrv
        else:
            pass
    
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