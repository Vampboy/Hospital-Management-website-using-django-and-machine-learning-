from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
#from .models import UserProfile
from .models import PatientDatabase , HospitalizedDataBase

class LoginForm(forms.Form):
   email = forms.CharField(max_length = 100,)
   password = forms.CharField()

class NameForm(forms.Form):
    Pno = forms.IntegerField(label='patient name')
    clerk_ID = forms.CharField(label='clerk name')
    Registration_Loc = forms.CharField(max_length=100,label='regis location')
    Register_Date_time = forms.DateField(label='date')
    HealthCare_no = forms.CharField(max_length=100,label='health id')
    first_name = forms.CharField( max_length=100,label='prakash')
    last_name = forms.CharField( max_length=100,label='last')
    Address = forms.CharField( max_length=200,label='add')
    city = forms.CharField( max_length=100,label='cit')
    state = forms.CharField( max_length=100,label='stat')
    zip_code = forms.CharField(max_length=100,label='zip')
    country = forms.CharField( max_length=100,label='con')
    phone_no_home = forms.CharField( max_length=100,label='phone')
    phone_no_work = forms.CharField( max_length=100,label='work')
    email = forms.EmailField(label='emaill')
    sex = forms.CharField(max_length=100,label='abcd')
    dob = forms.DateField(label='doob')
    Contact_first_name=forms.CharField(max_length=100,label='temp')
    Contact_last_name=forms.CharField(max_length=100,label='1temp')
    relationship=forms.CharField(max_length=100,label='temp1')
    Contact_Number=forms.CharField(max_length=100,label='temp2')
    description = forms.CharField(max_length=200,label='temp3')
    maritial_status = forms.CharField( max_length=100,label='temp4')
    age = forms.IntegerField(label='aage')
    CHOICES=(('護送進入','護送進入'),('護送進入','護送進入'),('護送進入','護送進入'))
    mode_arrival = forms.CharField(widget=forms.Select(choices=CHOICES),max_length=100,label='arrival')
    triage = forms.IntegerField(label='triag')
    blood_pressure = forms.IntegerField(label='bp' )
    body_temp = forms.CharField(label='bt')
    pulse = forms.IntegerField(label='pul')
    breath = forms.IntegerField(label='brth')

    
    def save(self):
        data = self.cleaned_data
        print("yooo")
        patientdatabase = PatientDatabase(
                                    Pno = data['Pno'],
                                    clerk_ID = data['clerk_ID'],
                                    Registration_Loc = data['Registration_Loc'],
                                    Register_Date_time =data['Register_Date_time'],
                                    HealthCare_no =data['HealthCare_no'],
                                    first_name =data['first_name'],
                                    last_name =data['last_name'],
                                    Address =data['Address'],
                                    city =data['city'],
                                    state =data['state'],
                                    zip_code =data['zip_code'],
                                    country =data['country'],
                                    phone_no_home =data['phone_no_home'],
                                    phone_no_work =data['phone_no_work'],
                                    email =data['email'],
                                    sex =data['sex'],
                                    dob =data['dob'],
                                    maritial_status =data['maritial_status'],       
                                    emer_first_name=data['Contact_first_name'],
                                    emer_last_name=data['Contact_last_name'],
                                    relationship=data['relationship'],
                                    emer_contact=data['Contact_Number'],
                                    description = data['description'],
                                    age = data['age'],
                                    mode_arrival = data['mode_arrival'],
                                    triage = data['triage'],
                                    blood_pressure = data['blood_pressure'],
                                    body_temp = data['body_temp'],
                                    pulse = data['pulse'],
                                    breathing = data['breath']
                                  )
        patientdatabase.save()

class Hospitalize_Form(forms.Form):
  Pno = forms.IntegerField()
  Caseno = forms.IntegerField()
  Entery_date = forms.DateField()
  Patient_name = forms.CharField(max_length=20)
  Doctor_name = forms.CharField(max_length=20)
  dob = forms.DateField()
  Department = forms.CharField(max_length=20)
  Admitting_date = forms.DateField()
  Remark = forms.CharField(max_length=20)
  Discharge_Date = forms.DateField()

  def save(self):
    #data = self.cleaned_data()
    #name_pno=PatientDatabase(Pno = self.cleaned_data["Pno"])

    hospitaldb = HospitalizedDataBase(
                                      Patient_no = self.cleaned_data["Pno"],
                                      Caseno = self.cleaned_data["Caseno"],
                                      Entery_date = self.cleaned_data["Entery_date"],
                                      Patient_name = self.cleaned_data["Patient_name"],
                                      Doctor_name =self.cleaned_data["Doctor_name"],
                                      dob = self.cleaned_data["dob"],
                                      Department = self.cleaned_data["Department"],
                                      Admitting_date = self.cleaned_data["Admitting_date"],
                                      Remark = self.cleaned_data["Remark"],
                                      Discharge_Date = self.cleaned_data["Discharge_Date"]
                                      )
    
    hospitaldb.save()