#importando superglobal para criação de view do django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
#importando modelos da pasta cadastros
from .models import Pta

from django.urls import reverse_lazy
# Criando as views que apareceram no site, baseadas nas models de cadastro usando o mesmo template



class PtaCreate(CreateView):
    #model q queremos criar a view
    model = Pta
    #campos do modelo que queremos usar
    fields = ['item', 'desc_item']
    #caminho do template que vai ser usado
    template_name = 'pta_form.html'
    #caminho que vai ser a URL quando for sucesso!
    success_url = reverse_lazy('index')  