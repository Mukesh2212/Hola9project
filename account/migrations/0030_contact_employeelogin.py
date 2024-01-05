# Generated by Django 4.0.3 on 2023-08-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_alter_jobapply_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
