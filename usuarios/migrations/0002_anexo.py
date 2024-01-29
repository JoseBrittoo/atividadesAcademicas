# Generated by Django 5.0.1 on 2024-01-28 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='anexos/')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.disciplina')),
            ],
        ),
    ]
