# Generated by Django 4.2.1 on 2023-05-27 06:15

from django.db import migrations, models
import siteapps.posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=siteapps.posts.models.upload_img_name),
        ),
    ]