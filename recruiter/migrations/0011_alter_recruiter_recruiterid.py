# Generated by Django 4.2.9 on 2024-04-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0010_alter_recruiter_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='recruiterId',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]