from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from myapi import views

urlpatterns = [
     re_path(r'^alumnos/$', views.AlumnoLista.as_view() ),
     re_path(r'^alumno/(?P<id>\d+)$', views.AlumnoDetalles.as_view() ),

     # Ulrs carrera
     re_path(r'^carreras/$', views.CarreraLista.as_view() ),
     re_path(r'^carrera/(?P<id>\d+)$', views.CarreraDetalles.as_view() ),      

     path('rest-auth/', include('rest_auth.urls')),
]

