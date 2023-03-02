
from django.contrib import admin
from django.urls import path , include

from .views import Actividades_Provincial_Mendoza , API_Actividades_Provincia_Mendoza

urlpatterns = [
    path('', Actividades_Provincial_Mendoza.as_view() , name="home_actividades_provincia_mendoza"),
    path('api_actividades_provincia_mendoza/', API_Actividades_Provincia_Mendoza.as_view() , name="api_actividades_provincia_mendoza"),
    
]
