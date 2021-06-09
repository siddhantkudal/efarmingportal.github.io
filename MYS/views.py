from django.shortcuts import render
from .models import mys
import datetime
# Create your views here.
def display(request):

    temp=mys.objects.all();
    
    temp2=datetime.datetime.now()
    
    return render(request,"mys.html",{'pdlist':temp,'time':temp2})



