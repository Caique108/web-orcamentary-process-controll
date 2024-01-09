from django.db import models

#Cadastro Pta
class Pta(models.Model):
    item = models.CharField(max_length=150,verbose_name="ITEM")
    desc_item = models.CharField(max_length=150, verbose_name="Descrição da Item" )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item'], name='item repetida')
        ]

    #Retorna a representação em STRING do objeto
    def __str__(self):
        return "{} ({})".format(self.item, self.desc_item)