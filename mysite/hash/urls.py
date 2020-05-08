from django.urls import path

from . import views

urlpatterns = [
    path('', views.hash, name='hash'),
    path('hash_encrypt/', views.HASH_Encryption, name='hash_encrypt'),
]