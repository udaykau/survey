from django.db import models
import os


def survey_file(instance, filename):
    os.path.join('media/SecureCare', instance.Email)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.Email, filename)
    return str(dire)


# Create your models here.
class survey(models.Model):
    sno = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=False)
    Applying_For = models.CharField(max_length=100)
    Applicant = models.CharField(max_length=300)
    Name = models.CharField(max_length=100)
    Care_Of = models.CharField(max_length=100)
    Father_Or_Husband_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    Communication_Address = models.CharField(max_length=100)
    Mobile_Number = models.CharField(max_length=30)
    Whatsapp_Number = models.CharField(max_length=30)
    Email = models.CharField(max_length=100)
    Self_photo = models.ImageField(null=True, blank=True, upload_to=survey_file)
    Adhar_Number = models.CharField(max_length=100)
    Adhar_Front = models.ImageField(null=True, blank=True, upload_to=survey_file)
    Adhar_Back = models.ImageField(null=True, blank=True, upload_to=survey_file)
    Pan_Number = models.CharField(max_length=100)
    Pan_Card = models.ImageField(null=True, blank=True, upload_to=survey_file)
    Bank_CSP_Center_Location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)