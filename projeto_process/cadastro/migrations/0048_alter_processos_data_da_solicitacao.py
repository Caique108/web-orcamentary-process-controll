# Generated by Django 4.2.6 on 2024-06-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0047_alter_processos_data_da_solicitacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='data_da_solicitacao',
            field=models.DateField(default='0000/00/00', verbose_name='Data da Solicitação'),
        ),
    ]
