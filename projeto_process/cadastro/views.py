#importando superglobal para criação de view do django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
#importando modelos da pasta cadastros
from .models import Campo,Processos,Fonte,Paoe

#chamada para para onde ir após a comfirmação na página
from django.urls import reverse_lazy

#trava as páginas para serem acessadas apenas com autenticação
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

# ---- Lembrando que essa página utilza os campos já criados no BD pelo arquivo "models.py" da referida pasta ----

#Criando as views referentes aos cadastros, exclusões e edições da aplicação, utilizando o "braces" para a filtragem entre as permissões dos usuários.

#Campo de Criação (Preenchimento/entry), dos dados.

class CampoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    #model q queremos criar a view
    model = Campo
    #campos do modelo que queremos usar
    fields = ['nome', 'descricao']
    #caminho do template que vai ser usado
    template_name = 'cadastros/form.html'
    #caminho que vai ser a URL quando for sucesso!
    success_url = reverse_lazy('index')

class ProcessosICreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
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

class FonteICreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fonte

    fields = [
        'fonte',
        'desc_fonte'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-fontes')

class PaoeICreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Paoe

    fields = [
        'paoe',
        'desc_paoe'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-paoe')

######### UPDATE #########
    
    #Campo de Edição dos dados criados pelo "Create".

class ProcessosIUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
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

class FonteIUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = Fonte

    fields = [
            'fonte',
            'desc_fonte'
            ]
    
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-fontes')

class PaoeIUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Paoe

    fields = [
        'paoe',
        'desc_paoe'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-paoe')




######### DELETE #########

#Campo de Exclusão dos dados já existentes.

class ProcessosIDelete(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = Processos

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-processos')

class FonteIDelete(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = Fonte

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-fontes')

class PaoeIDelete(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = Paoe

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-paoe')


######### LISTVIEW #########

#Campo da listagem das informações já preenchidas no BD

class ProcessosList (LoginRequiredMixin, ListView):

    login_url = reverse_lazy('login')
    model = Processos

    template_name = 'cadastros/listas/processos.html'

class FonteList (LoginRequiredMixin, ListView):

    login_url = reverse_lazy('login')
    model = Fonte

    template_name = 'cadastros/listas/fontes.html'

class PaoeList(LoginRequiredMixin, ListView):

    login_url = reverse_lazy('login')
    model = Paoe

    template_name = 'cadastros/listas/paoe.html'


