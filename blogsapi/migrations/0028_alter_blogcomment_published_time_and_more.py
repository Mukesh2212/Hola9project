# Generated by Django 4.0.3 on 2023-09-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapi', '0027_alter_blogcomment_email_alter_blogcomment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='published_time',
            field=models.CharField(default='2023-09-30', max_length=232),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='published_time',
            field=models.CharField(default='2023-09-30', max_length=150),
        ),
    ]