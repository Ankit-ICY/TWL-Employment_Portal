# Generated by Django 4.2.9 on 2024-04-03 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0008_rename_applicants_recruiter_selected_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiter.user_recruiter'),
        ),
    ]
