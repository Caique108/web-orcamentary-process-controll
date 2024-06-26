# Generated by Django 4.2.6 on 2024-04-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0035_alter_processos_valor_ind_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='valor_ind',
            field=models.DecimalField(decimal_places=2, max_digits=2000, verbose_name='Valor da Indicação'),
        ),
        migrations.AlterField(
            model_name='processos',
            name='valor_solicitado_ind',
            field=models.DecimalField(decimal_places=2, max_digits=2000, verbose_name='Valor Solicitado'),
        ),
    ]
