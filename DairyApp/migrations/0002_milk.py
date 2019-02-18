# Generated by Django 2.1.1 on 2018-10-10 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DairyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milk',
            fields=[
                ('date', models.DateField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DairyApp.Farmer', unique=True)),
                ('milkqty', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fat', models.DecimalField(decimal_places=1, max_digits=3)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('totalamt', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]