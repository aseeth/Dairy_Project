# Generated by Django 2.1.1 on 2018-10-10 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DairyApp', '0003_auto_20181010_2318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Milk',
            new_name='MilkData',
        ),
    ]