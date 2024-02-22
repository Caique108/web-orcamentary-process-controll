from django.db import models


# Create your models here.

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
    paoe = models.DecimalField(verbose_name="PAOE", max_digits=7, decimal_places=0)
    desc_paoe = models.CharField(max_length=150, verbose_name="Descrição da PAOE" )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['paoe'], name='paoe repetida')
        ]

    #Retorna a representação em STRING do objeto
    def __str__(self):
        return "{} ({})".format(self.paoe, self.desc_paoe)   
    
class Processos(models.Model):
    bbm = models.CharField(max_length=50, verbose_name="BBM")
    processo = models.CharField(max_length=150, verbose_name="Nº do Processo SEi")
    
    fonte2 = models.ForeignKey(Fonte, on_delete=models.PROTECT, verbose_name="Fonte")

    paoe2 = models.ForeignKey(Paoe, on_delete=models.PROTECT, verbose_name="PAOE")

    elemento = models.CharField(max_length=50)
    ano_da_indicação = models.DateField(help_text="Insira a data neste formato: <em>DD/MM/YYYY</em>.")
    valor_solicitado_ind = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Valor Solicitado" )
    valor_ind = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Valor da Indicação")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    contrato = models.CharField(max_length=150, verbose_name="Contrato", blank=True, null=True)
    
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['processo', 'ano_da_indicação'], name='processo do ano')
        ]

    #Retorna a representação em STRING do objeto
    def __str__(self):
        return "{} - Fonte({}) {} - {} - {}".format(self.bbm, self.fonte2.fonte, self.paoe2, self.campo.nome, self.campo.descricao)
    