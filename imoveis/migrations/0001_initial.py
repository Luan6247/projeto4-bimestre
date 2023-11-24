# Generated by Django 3.2.23 on 2023-11-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proprietario', models.CharField(max_length=50)),
                ('inquilino', models.CharField(max_length=50)),
                ('ContratoAluguel', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
