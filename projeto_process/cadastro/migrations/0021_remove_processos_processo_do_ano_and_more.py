# Generated by Django 4.2.6 on 2024-03-12 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0020_alter_processos_valor_solicitado_ind'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='processos',
            name='processo do ano',
        ),
        migrations.AlterField(
            model_name='processos',
            name='ano_da_indicação',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddConstraint(
            model_name='processos',
            constraint=models.UniqueConstraint(fields=('processo', 'ano_da_indicação', 'fonte2', 'paoe2'), name='processo do ano'),
        ),
    ]
