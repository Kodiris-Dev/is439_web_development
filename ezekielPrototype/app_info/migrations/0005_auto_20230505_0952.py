# Generated by Django 3.2.18 on 2023-05-05 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0004_rename_instructional_link_technique_youtube_embed_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beltpromotionpost',
            name='belt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='belt_promotion_posts', to='app_info.belt'),
        ),
        migrations.AlterField(
            model_name='beltpromotionpost',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='belt_promotion_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_info.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='app_info.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
