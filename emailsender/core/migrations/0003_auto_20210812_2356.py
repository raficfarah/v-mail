# Generated by Django 3.2.6 on 2021-08-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(max_length=65, verbose_name='nome do destinatário'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(blank=True, max_length=65, verbose_name='nome do remetente'),
        ),
    ]
