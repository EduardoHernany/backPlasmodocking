# Generated by Django 4.2.4 on 2023-11-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiocruz', '0017_macromoleculas_sem_redocking_delete_testes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='macro_prepare',
            name='processo_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]