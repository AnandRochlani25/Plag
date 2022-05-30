

#from django.conf.urls import include
#from django.conf.urls import repath as url
from django.urls import path
from django.conf.urls import include
from blog.views import generate_result1, get_report, home_page
#from blog import views as myapp_views
#from .views import generate_result,get_report,home_page

urlpatterns = [
 
    path('report/',generate_result1,name="rep"),
    path('record/',get_report,name="rec"),
    path('',home_page,name='home3'),
]
