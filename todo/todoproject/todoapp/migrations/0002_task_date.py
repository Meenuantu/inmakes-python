# Generated by Django 4.1.3 on 2022-11-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2021-03-20'),
            preserve_default=False,
        ),
    ]