# Generated by Django 4.1.5 on 2023-01-31 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0004_alter_person_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productqty', models.IntegerField(default=0)),
                ('is_checkout', models.BooleanField(default=0)),
                ('transaction_code', models.CharField(max_length=255, null=True)),
                ('Person_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.person')),
            ],
            options={
                'db_table': 'basket',
            },
        ),
    ]
