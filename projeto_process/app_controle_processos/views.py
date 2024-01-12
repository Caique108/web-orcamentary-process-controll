from django.shortcuts import render
from django.views.generic import TemplateView

from cadastro.views import CampoCreate


#Definindo os nomes de chamada para as URL's, e usar as mesmas na página urls.py   
def login(request):
    return render(request, 'paginas/login.html')  # RENDER (RENDERIZA UMA PÁGINA, CHAMANDO A PÁGINA)esse nome ao lado do request é a página HTML que vai vir no HOME!!
def painel(request):
    return render(request, 'paginas/painel.html')

def modelo(request):
    return render (request, 'paginas/modelo.html')

def home(request):
    return render (request, 'paginas/home.html')

def cadastro(request):
    return render (request, 'paginas/cadastro.html')




