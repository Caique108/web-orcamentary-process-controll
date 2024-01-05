# Generated by Django 4.2.6 on 2023-12-04 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Processos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbm', models.CharField(max_length=50, verbose_name='BBM')),
                ('processo', models.CharField(max_length=150, verbose_name='Processos')),
                ('fonte', models.IntegerField(verbose_name='Fonte')),
                ('elemento', models.CharField(max_length=50)),
                ('ano_da_indicação', models.DateField()),
                ('valor_solicitado_ind', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_ind', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('contrato', models.CharField(max_length=150, verbose_name='Contrato')),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.campo')),
            ],
        ),
    ]
