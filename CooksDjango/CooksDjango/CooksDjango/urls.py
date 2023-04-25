"""
Definition of urls for CooksDjango.
"""

from datetime import datetime
from xml.etree.ElementInclude import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path , include

from django.conf import Settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',include("Cooks.urls"))
]
