# Generated by Django 4.0.3 on 2023-12-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_delete_employeedetails_delete_employeelogin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='created_at',
            field=models.CharField(default='2023-12-10', max_length=150),
        ),
        migrations.AlterField(
            model_name='jobsrequired',
            name='created_at',
            field=models.CharField(default='2023-12-10', max_length=150),
        ),
        migrations.AlterField(
            model_name='reviewsection',
            name='created_at',
            field=models.CharField(default='2023-12-10', max_length=150),
        ),
        migrations.AlterField(
            model_name='telemetrydaa',
            name='date',
            field=models.CharField(default='2023-12-10', max_length=10),
        ),
    ]