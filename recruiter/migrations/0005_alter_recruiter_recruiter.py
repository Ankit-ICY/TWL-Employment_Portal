# Generated by Django 4.2.9 on 2024-03-28 16:10

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0004_alter_recruiter_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='recruiter',
            field=models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to='recruiter.user_recruiter'),
        ),
    ]
