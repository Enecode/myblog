# Generated by Django 4.1.3 on 2022-11-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blogs/featured_image/%Y/%m/%d/'),
        ),
    ]
