
from django.contrib import admin
from django.urls import path, include
from app_controle_processos import views
from django.views.generic import TemplateView

urlpatterns = [
    
    #rota, view responsável, nome de referência

    path('admin/', admin.site.urls),
    path('', include('app_controle_processos.urls')),
    #chamando as URLS direto das página urls do app e colocando no urls do django
    path('', include('cadastro.urls')),
    path('', include('usuarios.urls')),
    path('', include('planodetrabalho.urls')),
    
]
