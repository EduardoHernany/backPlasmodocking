# Generated by Django 4.2.4 on 2023-09-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiocruz', '0006_remove_arquivos_virtauls_resultado_final_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivos_virtauls',
            name='dada_docking',
        ),
        migrations.AddField(
            model_name='arquivos_virtauls',
            name='resultado_final',
            field=models.TextField(blank=True, null=True),
        ),
    ]
