from django.urls import path

from .views import CampoCreate, ProcessosICreate, FonteICreate,PaoeICreate,BBMICreate,ElementoICreate
from .views import ProcessosIUpdate, FonteIUpdate, PaoeIUpdate,BBMIUpdate,ElementoIUpdate
from .views import ProcessosIDelete, FonteIDelete, PaoeIDelete,BBMIDelete,ElementoIDelete
from .views import ProcessosList, FonteList, PaoeList,BBMList,ElementoList

# ----- Neste arquivo são deferidas as URLs que serão utilizadas nesta pasta, todas elas serão puxadas pela pasta do app principal no arquivo "configurações/urls.py". ----- 

# Colocar nessa variavel todos os teamplates que poderão ser chamados pela URL
urlpatterns = [
    
    #definindo como chamar cada página na URL

    # ---- CRIAÇÃO ---- #
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/processo/', ProcessosICreate.as_view(), name='cadastrar-processo'),
    path('cadastrar/fonte/', FonteICreate.as_view(), name='cadastrar-fonte'),
    path('cadastrar/paoe/', PaoeICreate.as_view(), name='cadastrar-paoe'),
    path('cadastrar/bbm/', BBMICreate.as_view(), name='cadastrar-bbm'),
    path('cadastrar/elemento/', ElementoICreate.as_view(), name='cadastrar-elemento'),
    

    # ---- EDIÇÃO ---- #
    #int(inteiro), pk(primarykey) - pk é o id do objeto
    path('editar/processo/<int:pk>/', ProcessosIUpdate.as_view(), name='editar-processo'),
    path('editar/fonte/<int:pk>/', FonteIUpdate.as_view(), name='editar-fonte'),
    path('editar/paoe/<int:pk>/', PaoeIUpdate.as_view(), name='editar-paoe'),
    path('editar/bbm/<int:pk>/', BBMIUpdate.as_view(), name='editar-bbm'),
    path('editar/bbm/<int:pk>/', BBMIUpdate.as_view(), name='editar-bbm'),
     path('editar/elemento/<int:pk>/', ElementoIUpdate.as_view(), name='editar-elemento'),


    # ---- EXCLUSÃO ---- #
    path('excluir/processo/<int:pk>/', ProcessosIDelete.as_view(), name='excluir-cadastro-ind'),
    path('excluir/fonte/<int:pk>/', FonteIDelete.as_view(), name='excluir-fonte'),
    path('excluir/paoe/<int:pk>/', PaoeIDelete.as_view(), name='excluir-paoe'),
    path('excluir/bbm/<int:pk>/', BBMIDelete.as_view(), name='excluir-bbm'),
    path('excluir/elemento/<int:pk>/', ElementoIDelete.as_view(), name='excluir-elemento'),

    # ---- LISTAS ---- #
    path('lista/processo/', ProcessosList.as_view(), name='listar-processo'),
    path('lista/fonte/', FonteList.as_view(), name='listar-fonte'),
    path('lista/paoe/', PaoeList.as_view(), name='listar-paoe'),
    path('lista/bbm/', BBMList.as_view(), name='listar-bbm'),
    path('lista/elemento/', ElementoList.as_view(), name='listar-elemento'),



]