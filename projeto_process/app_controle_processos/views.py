from django.shortcuts import render
from django.views.generic import TemplateView


<<<<<<< HEAD
#Definindo os nomes de chamada para as URL's, e usar as mesmas na página urls.py   
=======
#Definindo os nomes de chamada para as URL's, e usar as mesas na página urls.py   
>>>>>>> a7dfd785e40b8a9274d080c046c527b37a7cb2a1
def login(request):
    return render(request, 'paginas/login.html')  # RENDER (RENDERIZA UMA PÁGINA, CHAMANDO A PÁGINA)esse nome ao lado do request é a página HTML que vai vir no HOME!!
def painel(request):
    return render(request, 'paginas/painel.html')

def modelo(request):
    return render (request, 'paginas/modelo.html')

def home(request):
    return render (request, 'paginas/home.html')

def cadastro(request):
<<<<<<< HEAD
    return render (request, 'paginas/cadastro.html')

=======
    return render (request, 'paginas/cadastro.html')
>>>>>>> a7dfd785e40b8a9274d080c046c527b37a7cb2a1
