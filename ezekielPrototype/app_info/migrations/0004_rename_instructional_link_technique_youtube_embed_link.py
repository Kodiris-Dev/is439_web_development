# Generated by Django 3.2.18 on 2023-05-05 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0003_remove_profile_displayname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technique',
            old_name='instructional_link',
            new_name='youtube_embed_link',
        ),
    ]
