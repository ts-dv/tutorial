# Generated by Django 3.1.2 on 2020-10-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='ingredient_2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient_3',
            field=models.CharField(default='', max_length=30),
        ),
    ]
