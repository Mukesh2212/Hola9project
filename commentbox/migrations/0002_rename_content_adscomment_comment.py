# Generated by Django 4.0.3 on 2022-06-10 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adscomment',
            old_name='content',
            new_name='comment',
        ),
    ]
