# Generated by Django 4.2.9 on 2024-03-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0007_remove_work_work_category_work_work_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='applicants',
            name='expected_salary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applicants',
            name='phone_number',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='applicants',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
