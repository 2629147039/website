# Generated by Django 2.2 on 2020-08-14 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='has_confirmed',
        ),
        migrations.DeleteModel(
            name='ConfirmString',
        ),
    ]