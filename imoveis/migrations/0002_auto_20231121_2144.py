# Generated by Django 3.2.23 on 2023-11-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
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
        migrations.DeleteModel(
            name='Post',
        ),
    ]
