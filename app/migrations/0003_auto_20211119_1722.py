# Generated by Django 2.1.15 on 2021-11-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211118_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ctfd_configs',
            options={'verbose_name': 'Configurazione per la connessione CTFd', 'verbose_name_plural': 'Configurazioni per le connessioni CTFd'},
        ),
        migrations.AlterModelOptions(
            name='sshtunnel_configs',
            options={'verbose_name': 'Configurazione per la connessione alla macchina Docker', 'verbose_name_plural': 'Configurazioni per le connessioni alle macchine Docker'},
        ),
        migrations.AlterModelOptions(
            name='tag_level',
            options={'verbose_name': 'Livello di difficoltà per laboratorio', 'verbose_name_plural': 'Livelli di difficoltà per laboratori'},
        ),
        migrations.RemoveField(
            model_name='macchinaattacco',
            name='porta_ssh_esterna',
        ),
        migrations.RemoveField(
            model_name='macchinaattacco',
            name='porta_ssh_interna',
        ),
        migrations.AddField(
            model_name='user',
            name='porta_ssh',
            field=models.CharField(default='', max_length=5),
        ),
    ]