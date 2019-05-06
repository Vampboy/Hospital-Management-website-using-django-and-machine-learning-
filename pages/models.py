from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class PatientDatabase(models.Model):
    Pno = models.IntegerField(default=0,primary_key=True)
    clerk_ID = models.CharField(max_length=20,default=" ")
    description =models.CharField(max_length=10,default=' ')
    Register_Date_time = models.DateField(default=" ")
    HealthCare_no = models.CharField(max_length=10,default=" ")
    first_name = models.CharField(max_length=10,default=" ")
    last_name = models.CharField( max_length=10,default=" ")
    Address= models.CharField(max_length=200,default=" ")
    city = models.CharField( max_length=10,default=" ")
    Registration_Loc = models.CharField(max_length=10,default=" ")
    state = models.CharField(max_length=10,default=" ")
    zip_code = models.CharField(max_length=10,default=" ")
    country = models.CharField( max_length=10,default=" ")
    phone_no_home = models.CharField( max_length=10,default=" ")
    phone_no_work = models.CharField( max_length=10,default=" ")
    email = models.EmailField(default="")
    sex = models.CharField( max_length=10,default=" ")
    dob = models.DateField(default=" ")
    maritial_status = models.CharField( max_length=10,default=" ")
    emer_first_name=models.CharField(max_length=100,default=" ")
    emer_last_name=models.CharField(max_length=100,default=" ")
    relationship=models.CharField(max_length=100,default=" ")
    emer_contact=models.CharField(max_length=100,default=" ")
    age=models.IntegerField(default=0)
    mode_arrival =models.TextField(default=" ",max_length=100)
    triage = models.IntegerField(default=0)
    blood_pressure = models.IntegerField(default=0)
    body_temp = models.CharField(max_length=10,default=" ")
    pulse = models.IntegerField(default=0)
    breathing = models.IntegerField(default=0)
    hspt_prcnt = models.CharField(default=" ",max_length=10)
    not_h_prcnt = models.CharField(default=" ",max_length=10)

    
    
class HospitalizedDataBase(models.Model):
    Patient_no = models.IntegerField(default='0',primary_key=True)
    Caseno = models.IntegerField(default='0')
    Patient_name = models.CharField(max_length=20,default=" ")
    Doctor_name = models.CharField(max_length=20,default=" ")
    dob = models.DateField(default="1998-01-02")
    Entery_date = models.DateField(default="1998-01-02")
    Department = models.CharField(max_length=20,default=" ")
    Remark = models.CharField(max_length=20,default=" ")
    Admitting_date = models.DateField(default="1998-01-02")
    Discharge_Date = models.DateField(default="1998-01-02") 
    bed_alloted = models.CharField(default=" ",max_length=100)
    hspt_prcnt = models.CharField(default=" ",max_length=10)
    not_h_prcnt = models.CharField(default=" ",max_length=10)
    def __str__(self):
        return self.Caseno


class BedDataBase(models.Model):
    Bedname = models.CharField(default="unknown",max_length=100,primary_key=True)
    Gender_ward = models.CharField(default="",max_length=100)
    bed_type = models.CharField(default="",max_length=100)
    Bed_status = models.IntegerField(default=0)