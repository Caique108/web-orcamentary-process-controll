# Generated by Django 4.2.6 on 2024-04-03 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0031_remove_processos_processo_do_ano_processos_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='elemento2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastro.elemento', verbose_name='Elemento'),
        ),
    ]
