# Generated by Django 4.2.4 on 2023-12-12 16:05

from django.db import migrations, models
import fiocruz.models


class Migration(migrations.Migration):

    dependencies = [
        ('fiocruz', '0018_macro_prepare_processo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macro_prepare',
            name='ligantepdb',
            field=models.FileField(null=True, upload_to=fiocruz.models.arquivo),
        ),
        migrations.AlterField(
            model_name='macro_prepare',
            name='recptorpdbqt',
            field=models.FileField(null=True, upload_to=fiocruz.models.arquivo),
        ),
    ]
