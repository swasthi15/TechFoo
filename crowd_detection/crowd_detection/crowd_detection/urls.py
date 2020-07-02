from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import  static
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('signup/',views.signup),
    path('signup_submit/',views.signup_submit),
    path('login/',views.login),
    path('logging_in/',views.logging_in),
    path('location/',views.access_location),
    path('logout/',views.logout)]