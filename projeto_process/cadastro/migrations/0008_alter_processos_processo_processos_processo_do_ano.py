# Generated by Django 4.2.6 on 2023-12-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_alter_processos_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='processo',
            field=models.CharField(max_length=150, verbose_name='Nº do Processo SEi'),
        ),
        migrations.AddConstraint(
            model_name='processos',
            constraint=models.UniqueConstraint(fields=('processo', 'ano_da_indicação'), name='processo do ano'),
        ),
    ]