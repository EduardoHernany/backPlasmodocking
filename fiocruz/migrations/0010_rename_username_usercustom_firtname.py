# Generated by Django 4.2.4 on 2023-09-11 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiocruz', '0009_arquivos_virtauls_resultado_final'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercustom',
            old_name='username',
            new_name='firtname',
        ),
    ]
