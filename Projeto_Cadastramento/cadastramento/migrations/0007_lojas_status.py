# Generated by Django 5.0.6 on 2024-06-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastramento', '0006_alter_lojas_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='lojas',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendente'), ('approved', 'Aprovada'), ('rejected', 'Rejeitada')], default='pending', max_length=20),
        ),
    ]
