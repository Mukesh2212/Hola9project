# Generated by Django 4.0.3 on 2023-11-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapi', '0035_alter_blogcomment_published_time_alter_blogs_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='published_time',
            field=models.CharField(default='2023-11-04', max_length=232),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='published_time',
            field=models.CharField(default='2023-11-04', max_length=150),
        ),
    ]
