# Generated by Django 4.1.3 on 2022-11-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finch',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='finch',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]