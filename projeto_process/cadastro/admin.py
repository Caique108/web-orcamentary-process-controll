from django.contrib import admin

# Register your models here.
from .models import Campo, Processos, Fonte, Paoe
from planodetrabalho.models import Pta


admin.site.register(Campo)
admin.site.register(Processos)
admin.site.register(Fonte)
admin.site.register(Paoe)
admin.site.register(Pta)