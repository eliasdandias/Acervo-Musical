# Generated by Django 4.2.6 on 2023-11-06 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bandas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais_de_origem', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('pais_de_origem', models.CharField(max_length=50)),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcoes')),
            ],
        ),
        migrations.CreateModel(
            name='Musicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('interprete', models.CharField(max_length=50)),
                ('compositor', models.CharField(max_length=50)),
                ('ano_de_lancamento', models.CharField(max_length=50)),
                ('favoritar', models.CharField(max_length=50)),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bandas')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Biagrafia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia', models.CharField(max_length=50)),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bandas')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bandas')),
                ('musica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.musicas')),
            ],
        ),
    ]
