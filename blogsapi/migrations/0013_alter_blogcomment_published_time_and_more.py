# Generated by Django 4.0.3 on 2023-04-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapi', '0012_alter_blogcomment_published_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='published_time',
            field=models.CharField(default='2023-04-14', max_length=232),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='published_time',
            field=models.CharField(default='2023-04-14', max_length=150),
        ),
    ]
