# Generated by Django 4.2.4 on 2023-08-30 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiocruz', '0004_usercustom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivos_virtauls',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiocruz.usercustom'),
        ),
    ]
