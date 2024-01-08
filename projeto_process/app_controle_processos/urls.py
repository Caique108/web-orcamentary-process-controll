from django.urls import path
from .views import login, painel, modelo, home, cadastro



#colocar nessa variavel todos os teamplates que poderão ser chamados pela URL
urlpatterns = [
    #definindo como chamar cada página na URL
    
    path('painel/', painel, name='painel'),
    path('modelo/', modelo, name='modelo'),
    path('', home, name='home'),
    path('cadastros/', cadastro, name='cadastro')
<<<<<<< HEAD
    
=======
>>>>>>> a7dfd785e40b8a9274d080c046c527b37a7cb2a1

    
    
]