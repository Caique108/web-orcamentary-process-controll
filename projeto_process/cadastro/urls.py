from django.urls import path

from .views import CampoCreate, ProcessosICreate, FonteICreate,PaoeICreate
from .views import ProcessosIUpdate, FonteIUpdate, PaoeIUpdate
from .views import ProcessosIDelete, FonteIDelete, PaoeIDelete
from .views import ProcessosList, FonteList, PaoeList

#colocar nessa variavel todos os teamplates que poderão ser chamados pela URL
urlpatterns = [
    #definindo como chamar cada página na URL
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/processo/', ProcessosICreate.as_view(), name='cadastrar-indica'),
    path('cadastrar/fonte/', FonteICreate.as_view(), name='cadastrar-fonte'),
    path('cadastrar/paoe/', PaoeICreate.as_view(), name='cadastrar-paoe'),



    #int(inteiro), pk(primarykey) - chamadas do proprio django
    path('editar/processo/<int:pk>/', ProcessosIUpdate.as_view(), name='editar-cadastro-ind'),
    path('editar/fonte/<int:pk>/', FonteIUpdate.as_view(), name='editar-fonte'),
    path('editar/paoe/<int:pk>/', PaoeIUpdate.as_view(), name='editar-paoe'),




    path('excluir/processo/<int:pk>/', ProcessosIDelete.as_view(), name='excluir-cadastro-ind'),
    path('excluir/fonte/<int:pk>/', FonteIDelete.as_view(), name='excluir-fonte'),
    path('excluir/paoe/<int:pk>/', PaoeIDelete.as_view(), name='excluir-paoe'),


    path('lista/processo/', ProcessosList.as_view(), name='listar-processos'),
    path('lista/fonte/', FonteList.as_view(), name='listar-fontes'),
    path('lista/paoe/', PaoeList.as_view(), name='listar-paoe'),



]