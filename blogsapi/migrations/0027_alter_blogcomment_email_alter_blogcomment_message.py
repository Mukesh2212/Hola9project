# Generated by Django 4.0.3 on 2023-09-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapi', '0026_alter_blogcomment_published_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]