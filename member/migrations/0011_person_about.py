# Generated by Django 3.2.9 on 2023-07-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_remove_person_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='About',
            field=models.CharField(default=23, max_length=150),
            preserve_default=False,
        ),
    ]
