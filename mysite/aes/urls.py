from django.urls import path

from . import views

urlpatterns = [
    path('', views.aes, name='aes'),
    path('aes_encrypt/', views.AES_Encryption, name='aes_encrypt'),
    path('aes_decrypt/', views.AES_Decryption, name='aes_decrypt'),
]