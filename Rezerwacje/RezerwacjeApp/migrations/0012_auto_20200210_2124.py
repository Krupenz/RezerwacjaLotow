# Generated by Django 3.0.3 on 2020-02-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('RezerwacjeApp', '0011_auto_20200209_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasazerowie',
            name='pesel',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
