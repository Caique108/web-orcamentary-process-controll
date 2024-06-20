from django.urls import path
from .views import  painel, modelo, home, cadastro



#colocar nessa variavel todos os teamplates que poderão ser chamados pela URL
urlpatterns = [
    #definindo como chamar cada página na URL
    
    path('painel/', painel, name='painel'),
    path('modelo/', modelo, name='modelo'),
    path('', home, name='home'),
    path('cadastro', cadastro, name='cadastro'),
    
    

    
    
]