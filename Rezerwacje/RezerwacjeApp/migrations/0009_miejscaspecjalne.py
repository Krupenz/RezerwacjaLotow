# Generated by Django 3.0.3 on 2020-02-08 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('RezerwacjeApp', '0008_auto_20200208_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiejscaSpecjalne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siedzenie',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RezerwacjeApp.Siedzenia')),
                ('wymaganie',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RezerwacjeApp.Wymagania')),
            ],
        ),
    ]
