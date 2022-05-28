from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'app/default1.html')
    #return HttpResponse("<h1> How you doin <h1>")
