from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
import datetime




# Aqui criamos as classes que serão alocadas no sqlite3 e que também será chamado na página views para a definição das entrys e etc.


#essa classe foi usada como exemplo
class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    #  Retorna a representação em STRING do objeto
    def __str__(self):

        return "{} ({})".format(self.nome, self.descricao)
    
class Fonte(models.Model):
    fonte = models.DecimalField(verbose_name="Fonte", max_digits=3, decimal_places=0)
    desc_fonte = models.CharField(max_length=150, verbose_name="Descrição da fonte" )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fonte'], name='fonte repetida')
        ] 

    #Retorna a representação em STRING do objeto
    def __str__(self):
        return "{} ({})".format(self.fonte, self.desc_fonte)
    
class Paoe(models.Model):
    paoe = models.CharField(verbose_name="PAOE", max_length=150)
    desc_paoe = models.CharField(max_length=150, verbose_name="Descrição da PAOE" )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['paoe'], name='paoe repetida')
        ]

    #Retorna a representação em STRING do objeto
    def __str__(self):
        return "{} ({}) ".format(self.paoe, self.desc_paoe)   
    
class BBM(models.Model):
    desc_unidade = models.CharField(max_length=50, verbose_name="Descrição da Unidade", default="",help_text='Nome por extenso da unidade.')
    sigla_unidade = models.CharField(max_length=12, verbose_name="Sigla da Unidade", help_text='Exemplo: <strong>SCG</strong>.')

    localidade = models.CharField(max_length=30, verbose_name="Município", help_text="Localidade em que a UBM está situada.")

    def __str__(self):
        return "{} ({}) ".format(self.sigla_unidade, self.localidade)  

class Elemento(models.Model):
    
    elemento = models.CharField(max_length=30, verbose_name="Elemento")
    desc_elemento = models.CharField(max_length=250, verbose_name="Descrição do elemento")

    def __str__(self):
        return "{} ({}) ".format(self.elemento, self.desc_elemento)  

class Processos(models.Model):
    
    processo = models.CharField(max_length=150, verbose_name="Nº do Processo SEi")
    
    bbm2 = models.ForeignKey(BBM, on_delete=models.PROTECT, verbose_name="BBM")
    fonte2 = models.ForeignKey(Fonte, on_delete=models.PROTECT, verbose_name="Fonte")
    paoe2 = models.ForeignKey(Paoe, on_delete=models.PROTECT, verbose_name="PAOE")
    elemento2 = models.ForeignKey(Elemento, on_delete=models.PROTECT, verbose_name="Elemento", blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,)

    data_da_indicação = models.DateField(verbose_name="Data")
    valor_solicitado_ind = models.CharField(max_length=2000, verbose_name="Valor Solicitado", default="R$0,00", )
    valor_ind = models.CharField(max_length=2000, verbose_name="Valor da Indicação", default="R$0,00")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    contrato = models.CharField(max_length=150, verbose_name="Contrato", blank=True, null=True)
    

    # relaciona a classe ao usuario, podendo visualizar apenas oque o usuario lançou
    # usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['processo', 'data_da_indicação','fonte2','paoe2','bbm2'], name='processo do ano')
    #     ]

    #Retorna a representação em STRING do objeto
    def __str__(self):
        return "{} - Fonte({}) {} - {} - {}".format(self.bbm2, self.fonte2.fonte, self.paoe2, self.campo.nome, self.campo.descricao)
    
 