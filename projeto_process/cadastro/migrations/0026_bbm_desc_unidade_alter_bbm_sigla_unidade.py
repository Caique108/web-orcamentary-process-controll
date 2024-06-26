# Generated by Django 4.2.6 on 2024-03-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0025_remove_processos_processo_do_ano_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbm',
            name='desc_unidade',
            field=models.CharField(default='', max_length=50, verbose_name='Descrição da Unidade'),
        ),
        migrations.AlterField(
            model_name='bbm',
            name='sigla_unidade',
            field=models.CharField(help_text='SCG', max_length=12, verbose_name='Sigla da Unidade'),
        ),
    ]
