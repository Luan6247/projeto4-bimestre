# Generated by Django 3.2.23 on 2023-11-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.CharField(choices=[('aluguel', 'aluguel'), ('Venda', 'Venda')], max_length=255)),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=10, max_digits=19)),
                ('cliente', models.TextField(max_length=255)),
                ('corretor', models.TextField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
