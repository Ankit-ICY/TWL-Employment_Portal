# Generated by Django 4.2.9 on 2024-03-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_alter_applicants_gender_alter_applicants_job_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='expected_salary',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]