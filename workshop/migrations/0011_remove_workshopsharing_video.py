# Generated by Django 3.2.9 on 2023-07-09 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0010_inbox_is_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopsharing',
            name='Video',
        ),
    ]
