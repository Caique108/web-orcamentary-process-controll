#importando superglobal para criação de view do django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
#importando modelos da pasta cadastros
from .models import Campo,Processos,Fonte,Paoe

from django.urls import reverse_lazy
# Criando as views que apareceram no site, baseadas nas models de cadastro usando o mesmo template

class CampoCreate(CreateView):
    #model q queremos criar a view
    model = Campo
    #campos do modelo que queremos usar
    fields = ['nome', 'descricao']
    #caminho do template que vai ser usado
    template_name = 'cadastros/form.html'
    #caminho que vai ser a URL quando for sucesso!
    success_url = reverse_lazy('index')


class ProcessosICreate(CreateView):
    model = Processos

    fields = [
            'bbm' ,
            'processo' ,
            'fonte2' ,
            'paoe2',
            'elemento' ,
            'ano_da_indicação' ,
            'valor_solicitado_ind' ,
            'valor_ind' ,
            'descricao' ,
            'contrato' ,
            'campo'
            ]
    
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-processos')

class FonteICreate(CreateView):
    model = Fonte

    fields = [
        'fonte',
        'desc_fonte'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-fontes')


class PaoeICreate(CreateView):
    model = Paoe

    fields = [
        'paoe',
        'desc_paoe'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-paoe')



######### UPDATE #########

class ProcessosIUpdate(UpdateView):
    model = Processos

    fields = [
            'bbm' ,
            'processo' ,
            'fonte2' ,
            'paoe2',
            'elemento' ,
            'ano_da_indicação' ,
            'valor_solicitado_ind' ,
            'valor_ind' ,
            'descricao' ,
            'contrato' ,
            'campo'
            ]
    
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-processos')


class FonteIUpdate(UpdateView):
    model = Fonte

    fields = [
            'fonte',
            'desc_fonte'
            ]
    
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-fontes')



class PaoeIUpdate(UpdateView):
    model = Paoe

    fields = [
        'paoe',
        'desc_paoe'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-paoe')




######### DELETE #########



class ProcessosIDelete(DeleteView):
    model = Processos

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-processos')



class FonteIDelete(DeleteView):
    model = Fonte

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-fontes')



class PaoeIDelete(DeleteView):
    model = Paoe

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-paoe')




######### LISTVIEW #########


class ProcessosList (ListView):
    model = Processos

    template_name = 'cadastros/listas/processos.html'

class FonteList (ListView):
    model = Fonte

    template_name = 'cadastros/listas/fontes.html'


class PaoeList(ListView):
    model = Paoe

    template_name = 'cadastros/listas/paoe.html'


