# Generated by Django 3.2.18 on 2023-03-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0003_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='banner_picture',
            field=models.ImageField(default='', upload_to='app_info/banner_pictures/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='app_info/profile_pictures/'),
        ),
    ]