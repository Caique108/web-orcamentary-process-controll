from django.urls import path

from .views import CampoCreate, ProcessosICreate, FonteICreate,PaoeICreate
from .views import ProcessosIUpdate, FonteIUpdate, PaoeIUpdate
from .views import ProcessosIDelete, FonteIDelete, PaoeIDelete
from .views import ProcessosList, FonteList, PaoeList

# ----- Neste arquivo são deferidas as URLs que serão utilizadas nesta pasta, todas elas serão puxadas pela pasta do app principal no arquivo "configurações/urls.py". ----- 

# Colocar nessa variavel todos os teamplates que poderão ser chamados pela URL
urlpatterns = [
    
    #definindo como chamar cada página na URL

    # ---- CRIAÇÃO ---- #
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/processo/', ProcessosICreate.as_view(), name='cadastrar-indica'),
    path('cadastrar/fonte/', FonteICreate.as_view(), name='cadastrar-fonte'),
    path('cadastrar/paoe/', PaoeICreate.as_view(), name='cadastrar-paoe'),
    

    # ---- EDIÇÃO ---- #
    #int(inteiro), pk(primarykey) - pk é o id do objeto
    path('editar/processo/<int:pk>/', ProcessosIUpdate.as_view(), name='editar-cadastro-ind'),
    path('editar/fonte/<int:pk>/', FonteIUpdate.as_view(), name='editar-fonte'),
    path('editar/paoe/<int:pk>/', PaoeIUpdate.as_view(), name='editar-paoe'),

    # ---- EXCLUSÃO ---- #
    path('excluir/processo/<int:pk>/', ProcessosIDelete.as_view(), name='excluir-cadastro-ind'),
    path('excluir/fonte/<int:pk>/', FonteIDelete.as_view(), name='excluir-fonte'),
    path('excluir/paoe/<int:pk>/', PaoeIDelete.as_view(), name='excluir-paoe'),

    # ---- LISTAS ---- #
    path('lista/processo/', ProcessosList.as_view(), name='listar-processos'),
    path('lista/fonte/', FonteList.as_view(), name='listar-fontes'),
    path('lista/paoe/', PaoeList.as_view(), name='listar-paoe'),



]