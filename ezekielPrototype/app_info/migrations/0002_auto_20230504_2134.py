# Generated by Django 3.2.18 on 2023-05-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beltpromotionpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
