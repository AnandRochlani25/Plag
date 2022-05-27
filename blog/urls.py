
from django.urls import path
from django.urls import path
from .views import generate_result,get_report,home_page

urlpatterns = [
 
    path('report/',generate_result,name="rep"),
    path('record/',get_report,name="rec"),
    path('',home_page,name='home')
]