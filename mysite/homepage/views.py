from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def homepage(request):
    return render(request,'homepage/homepage.html')

def Error404(request, exception):
    return render(request,'homepage/error.html', {'message': exception}, status = 404)

def Error500(request):
    return render(request,'homepage/error.html', status = 500)
