from django.urls import path

from . import views

urlpatterns = [
    path('', views.rsa, name='rsa'),
    path('generateKey/', views.generateKey, name='generateKey'),
    path('rsa_encrypt/', views.encrypt, name='rsa_encrypt'),
    path('rsa_decrypt/', views.decrypt, name='rsa_decrypt'),
   
]