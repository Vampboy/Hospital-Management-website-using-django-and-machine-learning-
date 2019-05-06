from django.urls import path
from django.conf.urls import url, include

from . import views 
urlpatterns = [

    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('patient_registration/',views.patient_registration,name='patient_registration'),
    path('health_pred/',views.health_pred,name='health_pred'),
    path('newpatient/',views.newpatient,name='newpatient'),
    path('Hospitalization_form/',views.Hospitalization_form,name='Hospitalization_form'),
    path('Patient_search/',views.Patient_search,name='Patient_search'),
    path('Patient_data/',views.Patient_data,name='Patient_data'),
    path('Django_regis',views.Django_regis,name='Django_regis'),
    path('bed-availability',views.bed_availability,name='bed-availability'),
    path('delete',views.delete,name='delete'),
    path('report',views.report,name='report'),

    #path('bed-availability',views.bed_availability,name='bed_availability'),    
    #path('database_list',views.database_list,name='database_list'),


]



