# Generated by Django 5.0.6 on 2024-06-07 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastramento', '0003_alter_produtos_codigo_da_roupa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='loja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastramento.lojas'),
        ),
    ]
