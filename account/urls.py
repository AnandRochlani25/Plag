from django.urls import path
from .views import generate_report,home_page,get_report


urlpatterns = [
 
    path('report/',generate_report,name="unit2rep"),
    path('record/',get_report,name="unit2rec"),
    path('',home_page,name='home')
    
   
]