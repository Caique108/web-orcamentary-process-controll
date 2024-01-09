from django.urls import path

from .views import PtaCreate


#colocar nessa variavel todos os teamplates que poderão ser chamados pela URL

urlpatterns = [
    #definindo como chamar cada página na URL
  path('cadastrar/pta/', PtaCreate.as_view(), name='cadastrar-pta'),]