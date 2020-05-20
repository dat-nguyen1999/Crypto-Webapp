from django.urls import path

from . import views

urlpatterns = [
    path('', views.des, name='tdes'),
    path('tdes_encrypt/', views.TDES_Encryption, name='tdes_encrypt'),
    path('tdes_decrypt/', views.TDES_Decryption, name='tdes_decrypt'),
]