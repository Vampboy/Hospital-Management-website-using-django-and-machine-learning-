from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
import os
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from sklearn.externals import joblib


def home(request):
   return render(request, 'home.html', {})



def index(request):
    return render(request,"index.html",{})

def bed_availability(request):
    if request.method == 'POST':
            Ward_gender = request.POST.get("ward-gender")
            bed_type = request.POST.get("bed-type")


            print(Ward_gender)
            print(bed_type)

            bed_free= BedDataBase.objects.filter(Gender_ward=Ward_gender,bed_type=bed_type,Bed_status=0)
            print(len(bed_free))

            bed_id=bed_free[0].Bedname
            print(bed_id)

            temp=HospitalizedDataBase.objects.filter(Patient_no=passpid)
            print(yoo)
            BedDataBase.objects.filter(Bedname=bed_id).update(Bed_status=1)
            HospitalizedDataBase.objects.filter(Patient_no=passpid).update(bed_alloted=bed_id)  

            

            return render(request,'bed-availability.html',{ })
    else:
            form=10
            return render(request,'bed-availability.html',{})    


from .forms import NameForm , Hospitalize_Form
from .models import PatientDatabase ,HospitalizedDataBase ,BedDataBase
def patient_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        print('check')
        if form.is_valid():
                print("yoo")
            # process the data in form.cleaned_data as required
                form.save()
                print(form.cleaned_data.get('Pno'))
                print(form.cleaned_data.get('mode_arrival'))
                #static Prediction
                from NeuralNetwork.Neural_predictor import Hospital_pred 
                
                Static_check=Hospital_pred()
                temp=np.array([[
                        form.cleaned_data.get('age'),
                        form.cleaned_data.get('mode_arrival'),
                        form.cleaned_data.get('triage'),
                        form.cleaned_data.get('blood_pressure'),
                        form.cleaned_data.get('pulse'),
                        form.cleaned_data.get('breath'),
                        float(form.cleaned_data.get('body_temp'))
                ]])
                #temp1=np.array([[19,'護送進入',2,149,87,18,36.7]])
                #print(temp)
                #print(temp1)
                
                labelencoder = joblib.load("NeuralNetwork/labelencoder.save") 
                temp[:,1] = labelencoder.transform(temp[:,1])
                #print(temp)
                #print(np.shape(temp))
                pred=float(Static_check.getpredictor(temp))
                
                # pred>0.5 100% admit condition 
                if pred>0.5:
                        percent=100
                else:
                        percent=(pred/0.5)*100        

                percent= float("{0:.2f}".format(percent))
                not_prcnt=100-percent
                temp=form.cleaned_data.get('Pno')
                hos_red=HospitalizedDataBase(Patient_no=temp,hspt_prcnt=str(percent),not_h_prcnt=str(not_prcnt))
                hos_red.save()
                #print(hos_red.clean_data.get('hspt_prcnt'))
                
                
                PatientDatabase.objects.filter(Pno=temp).update(hspt_prcnt=str(percent))
                PatientDatabase.objects.filter(Pno=temp).update(not_h_prcnt=str(not_prcnt))


                #percent=0
                Patient= PatientDatabase.objects.get(Pno=temp)
                arg={'percent':percent,'value': Patient}
            # redirect to a new URL:
                return render(request, 'health_pred.html', arg)

    # if a GET (or any other method) we'll create a blank form
    else:
                #patient_id=request.GET.get('pid')
                #print(patient_id)
                #Patient= PatientDatabase.objects.get(Pno=patient_id)
                form = NameForm()

    return render(request, 'patient_registration.html', {'form': form})

def newpatient(request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                form = NameForm(request.POST)
                # check whether it's valid:
                print('check')
                if form.is_valid():
                # process the data in form.cleaned_data as required
                        print(form.cleaned_data.get('breath'))
                        form.save()
                # redirect to a new URL:
                        return HttpResponseRedirect('')

        # if a GET (or any other method) we'll create a blank form
        else:
                form = NameForm()

                return render(request, 'newpatient.html', {'form':form})


def health_pred(request):
        if request.method == 'POST':
                form = Hospitalize_Form(request.POST)
                print('check')
                #if form.is_valid():
                #        print("tdth")
                #        form.save()
                ## redirect to a new URL:
                #        passpid=form.cleaned_data.get('Pno')
        percent=0
        return render(request, 'health_pred.html', {'percent': percent})

def Hospitalization_form(request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                form = Hospitalize_Form(request.POST)

                # check whether it's valid:
                print('check')
                #print(form.Pno)
                if form.is_valid():
                # process the data in form.cleaned_data as required
                        #print(form.Pno)
                        hsp=" "
                        nhspt=" "
                        print("tdth")
                        passpid=form.cleaned_data.get('Pno')
                        store=HospitalizedDataBase.objects.filter(Patient_no=passpid)
                        if len(store)==1:
                                hsp=store[0].hspt_prcnt
                                nhspt=store[0].not_h_prcnt
                        form.save()
     
                
                # redirect to a new URL:

                        Ward_gender = request.POST.get("ward-gender")
                        bed_type = request.POST.get("bed-type")


                        print(Ward_gender)
                        print(bed_type)

                        bed_free= BedDataBase.objects.filter(Gender_ward=Ward_gender,bed_type=bed_type,Bed_status=0)
                        print(len(bed_free))

                        bed_id=bed_free[0].Bedname
                        print(bed_id)

                        HospitalizedDataBase.objects.filter(Patient_no=passpid).update(bed_alloted=bed_id,hspt_prcnt=hsp,not_h_prcnt=nhspt)  
                        BedDataBase.objects.filter(Bedname=bed_id).update(Bed_status=1)

                        temp=form.cleaned_data.get('Pno')
                        value= HospitalizedDataBase.objects.get(Patient_no=temp)
                        print(value.Patient_no)

                        arg={'value':value,'tat':123}

                        return  render(request,'bed-availability.html',arg)

        # if a GET (or any other method) we'll create a blank form
        else:
                form = Hospitalize_Form()

                available_beds= BedDataBase.objects.filter(Bed_status=0)
                available_beds=len(available_beds)

                Male_delux= BedDataBase.objects.filter(Gender_ward="Male",bed_type="Deluxe",Bed_status=0)
                Male_delux = len(Male_delux)

                Female_delux= BedDataBase.objects.filter(Gender_ward="Female",bed_type="Private",Bed_status=0)
                Female_delux = len(Female_delux)

                Male_Private = BedDataBase.objects.filter(Gender_ward="Male",bed_type="General",Bed_status=0)
                Male_Private = len(Male_Private)

                Female_Private = BedDataBase.objects.filter(Gender_ward="Female",bed_type="Deluxe",Bed_status=0)
                Female_Private = len(Female_Private)

                Male_General = BedDataBase.objects.filter(Gender_ward="Male",bed_type="Private",Bed_status=0)
                Male_General = len(Male_General)

                Female_General = BedDataBase.objects.filter(Gender_ward="Male",bed_type="General",Bed_status=0)
                Female_General = len(Female_General)

                print(available_beds,Male_General,Male_Private,Male_delux,Female_General,Female_Private,Female_delux)               


                arg={'form':form,'available_beds':available_beds,
                'Male_General':Male_General,'Male_Private':Male_Private,'Male_deluxe':Male_delux,
                'Female_General':Female_General,'Female_Private':Female_Private,'Female_deluxe':Female_delux}


                return render(request,'Hospitalization_form.html',arg)

def Patient_search(request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                Patient_id1 = request.POST.get("pid1")
                Patient_id2 =request.POST.get("pid2")
                # check whether it's valid:
                form = NameForm()
                print(Patient_id1,Patient_id2)
                if Patient_id1:
                        Patient= PatientDatabase.objects.get(Pno=Patient_id1)
                        return render(request,'Patient_data.html',{'value': Patient})

                else:
                        Patient= HospitalizedDataBase.objects.get(Patient_no=Patient_id2)
                # redirect to a new URL:
                        return render(request,'bed-availability.html',{'value': Patient})

        # if a GET (or any other method) we'll create a blank form
        else:
                return render(request,'Patient_search.html',{})

def Patient_data(request):
        
        temp= PatientDatabase.objects.get(Pno=1)
        print(temp.first_name)
        return render(request,'Patient_data.html',{})

def Django_regis(request):        
      form = Hospitalize_Form(request.GET)
      return render(request,'Django_regis.html',{'form':form})

def delete(request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                Patient_id = request.POST.get("pid")
                # check whether it's valid:
                print(Patient_id)
                Patient= PatientDatabase.objects.filter(Pno=Patient_id)
                if len(Patient)>=1:

                        PatientDatabase.objects.filter(Pno=Patient_id).delete()
                        msg="Entered Pno data deleted"
                else:

                        msg="Invalid PNO"
                Patient= HospitalizedDataBase.objects.filter(Patient_no=Patient_id)
                if len(Patient)>=1:
                        Bed_id=Patient[0].bed_alloted
                        print(Bed_id)
                        BedDataBase.objects.filter(Bedname=Bed_id).update(Bed_status=0)
                        HospitalizedDataBase.objects.filter(Patient_no=Patient_id).delete()
                        msg="Entered Pno data deleted"


                # redirect to a new URL:
                return render(request,'delete.html',{'msg': msg})

        # if a GET (or any other method) we'll create a blank form
        else:
                msg="Enter the Pno of the record to be deleted"
                return render(request,'delete.html',{'msg':msg})


def report(request):
        return render(request,'report.html',{})