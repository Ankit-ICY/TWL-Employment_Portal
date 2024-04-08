# Generated by Django 5.0.3 on 2024-03-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('applicant_id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(choices=[('hindi', 'Hindi'), ('english', 'English')], max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photo')),
                ('full_name', models.CharField(max_length=60)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('location', models.CharField(max_length=60)),
                ('job_title', models.CharField(max_length=60)),
                ('experience', models.IntegerField(default=None)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(max_length=5)),
                ('job_time', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], max_length=12)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('skills', models.CharField(default='', max_length=100)),
            ],
        ),
    ]