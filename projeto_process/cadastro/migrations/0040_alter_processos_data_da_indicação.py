# Generated by Django 4.2.6 on 2024-06-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0039_alter_processos_valor_ind_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='data_da_indicação',
            field=models.DateField(verbose_name='Data da indicação'),
        ),
    ]
