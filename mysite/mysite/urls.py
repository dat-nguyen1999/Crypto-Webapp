"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', include('homepage.urls')),
    path('des/', include('des.urls')),
    path('hash/', include('hash.urls')),
    path('tdes/', include('tdes.urls')),
    path('aes/', include('aes.urls')),
    path('rsa/', include('rsa.urls')),

]
urlpatterns += staticfiles_urlpatterns()   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404= 'homepage.views.Error404'
handler500= 'homepage.views.Error500'

