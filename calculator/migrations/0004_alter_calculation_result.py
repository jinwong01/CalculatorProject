# Generated by Django 3.2.4 on 2021-06-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_alter_calculation_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='result',
            field=models.CharField(max_length=9),
        ),
    ]