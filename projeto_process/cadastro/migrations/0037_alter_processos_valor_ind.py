# Generated by Django 4.2.6 on 2024-05-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0036_alter_processos_valor_ind_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='valor_ind',
            field=models.CharField(max_length=2000, verbose_name='Valor da Indicação'),
        ),
    ]
