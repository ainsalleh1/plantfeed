# Generated by Django 3.2.9 on 2023-04-02 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_rename_password_person_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='username',
            new_name='Username',
        ),
    ]
