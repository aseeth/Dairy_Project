# Generated by Django 2.1.1 on 2018-10-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DairyApp', '0004_auto_20181010_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milkdata',
            name='fid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DairyApp.Farmer'),
        ),
    ]
