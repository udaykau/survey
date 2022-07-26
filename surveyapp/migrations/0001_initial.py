# Generated by Django 3.1.6 on 2022-07-23 14:11

from django.db import migrations, models
import surveyapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='survey',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Applicant', models.CharField(max_length=300)),
                ('Name', models.CharField(max_length=100)),
                ('Care_Of', models.CharField(max_length=100)),
                ('Father_Or_Husband_Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('DOB', models.CharField(max_length=100)),
                ('Communication_Address', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=30)),
                ('Whatsapp_Number', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=100)),
                ('Self_photo', models.ImageField(blank=True, null=True, upload_to=surveyapp.models.survey_file)),
                ('Adhar_Number', models.CharField(max_length=100)),
                ('Adhar_Front', models.ImageField(blank=True, null=True, upload_to=surveyapp.models.survey_file)),
                ('Adhar_Back', models.ImageField(blank=True, null=True, upload_to=surveyapp.models.survey_file)),
                ('Pan_Number', models.CharField(max_length=100)),
                ('Pan_Card', models.ImageField(blank=True, null=True, upload_to=surveyapp.models.survey_file)),
                ('Bank_CSP_Center_Location', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
