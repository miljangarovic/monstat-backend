from django.shortcuts import render
from .models import Stanovnik
import json
# Create your views here.


def show_all_people(request):
    return render(request,'test.html',context={'test':Stanovnik.objects.all()})