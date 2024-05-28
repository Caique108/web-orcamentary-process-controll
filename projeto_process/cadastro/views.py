#importando superglobal para criação de view do django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
# ---- GrouprequiredMixin, controla quais páginas os usuarios de certo grupo podem acessar
from braces.views import GroupRequiredMixin
#trava as páginas para serem acessadas apenas com autenticação
from django.contrib.auth.mixins import LoginRequiredMixin
#chamada para para onde ir após a comfirmação na página
from django.urls import reverse_lazy





#____#importando modelos da pasta cadastros_______#
    
from .models import Campo,Processos,Fonte,Paoe,BBM,Elemento





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

class ProcessosICreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'DEPLAN',]
    model = Processos
    fields = ['processo',
            'valor_solicitado_ind',
            'descricao',
            'bbm2',
            'fonte2',
            'paoe2',
            'elemento2',
            'data_da_indicação',
            'valor_ind',
            'contrato',
            'campo']

    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-processo')
    
    def form_valid(self, form):
        #Pegando o usuario que fez a requisição da classe user do django
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url
    

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

class BBMICreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = BBM

    fields = [
        'desc_unidade',
        'sigla_unidade',
        'localidade',

    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-bbm')


class ElementoICreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Elemento

    fields = [
        'elemento',
        'desc_elemento',
        
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-elemento')

######### UPDATE #########
    
    #Campo de Edição dos dados criados pelo "Create".

class ProcessosIUpdate(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = Processos

    fields = [
            'processo',
            'valor_solicitado_ind',
            'descricao',
            'bbm2',
            'fonte2',
            'paoe2',
            'elemento2',
            'data_da_indicação',
            'valor_ind',
            'contrato',
            'campo'
            ]
    
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-processo')

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

class BBMIUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = BBM

    fields = [
        'sigla_unidade',
        'localidade'
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-bbm')

class ElementoIUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Elemento

    fields = [
        'elemento',
        'desc_elemento',
        
    ]
    template_name = 'cadastros/form.html'

    success_url = reverse_lazy('listar-elemento')


######### DELETE #########

#Campo de Exclusão dos dados já existentes.

class ProcessosIDelete(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = Processos

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-processo')

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

class BBMIDelete(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = BBM

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-bbm')

class ElementoIDelete(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    model = Elemento

    template_name = 'cadastros/form-excluir.html'

    success_url = reverse_lazy('listar-elemento')


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

class BBMList(LoginRequiredMixin, ListView):

    login_url = reverse_lazy('login')
    model = BBM

    template_name = 'cadastros/listas/bbm.html'

class ElementoList(LoginRequiredMixin, ListView):

    login_url = reverse_lazy('login')
    model = Elemento

    template_name = 'cadastros/listas/elemento.html'


