# Generated by Django 5.0.1 on 2024-01-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='popularity',
            field=models.IntegerField(),
        ),
    ]