from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Settings


def index(request):
    setting=Settings.objects.get(pk=1)
    context={'setting':setting,'page':'home'}

    return render(request,'index.html',context)

def aboutus(request):
    setting=Settings.objects.get(pk=1)
    context={'setting':setting,'page':'aboutus'}

    return render(request,'aboutus.html',context)

def references(request):
    setting=Settings.objects.get(pk=1)
    context={'setting':setting,'page':'references'}

    return render(request,'references.html',context)

def contactus(request):
    setting=Settings.objects.get(pk=1)
    context={'setting':setting,'page':'contactus'}

    return render(request,'contactus.html',context)