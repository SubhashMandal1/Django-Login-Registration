# Generated by Django 4.2.1 on 2023-05-19 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_log', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cred',
            new_name='UserCreds',
        ),
    ]
