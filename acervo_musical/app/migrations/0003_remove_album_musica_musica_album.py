# Generated by Django 4.2.6 on 2023-11-14 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banda_rename_cadastros_cadastro_remove_musicas_banda_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musica',
        ),
        migrations.AddField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.album'),
            preserve_default=False,
        ),
    ]
