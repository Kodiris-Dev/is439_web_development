# Generated by Django 3.2.18 on 2023-05-05 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0002_auto_20230504_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='displayName',
        ),
    ]
