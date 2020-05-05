from django.urls import path

from . import views

urlpatterns = [
    path('', views.hash, name='hash'),
    path('hash_encrypt/', views.HASH_Encryption, name='hash_encrypt'),
    path('hash_decrypt/', views.HASH_Decryption, name='hash_decrypt'),
]