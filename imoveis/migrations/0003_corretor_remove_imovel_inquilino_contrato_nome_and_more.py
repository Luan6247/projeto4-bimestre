# Generated by Django 4.2.7 on 2023-12-03 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_auto_20231128_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('numero', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='inquilino',
        ),
        migrations.AddField(
            model_name='contrato',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imovel',
            name='endereco',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='imovel',
            name='imagem',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imovel',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imoveis.usuario'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='ContratoAluguel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.contrato'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imoveis.usuario'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='corretor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.corretor'),
        ),
    ]
