# Generated by Django 4.2.6 on 2023-12-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_processos_fonte2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fonte',
            name='fonte',
            field=models.IntegerField(max_length=3, verbose_name='Fonte'),
        ),
    ]
