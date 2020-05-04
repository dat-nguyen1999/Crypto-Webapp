from django.urls import path

from . import views

urlpatterns = [
    path('', views.des, name='des'),
    path('des_encrypt/', views.DES_Encryption, name='des_encrypt'),
    path('des_decrypt/', views.DES_DEcryption, name='des_decrypt'),
]