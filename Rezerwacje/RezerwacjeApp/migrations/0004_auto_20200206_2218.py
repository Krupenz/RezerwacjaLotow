# Generated by Django 3.0.3 on 2020-02-06 21:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('RezerwacjeApp', '0003_auto_20200206_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rezerwacje',
            old_name='id_pasazera',
            new_name='pasazer',
        ),
    ]
