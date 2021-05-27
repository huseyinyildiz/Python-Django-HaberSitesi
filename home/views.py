from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Settings, ContactFormu, ContactFormMessage
from news.models import New, Category


def index(request):
    setting=Settings.objects.get(pk=1)
    sliderdata =New.objects.all()[:4]
    category=Category.objects.all()
    context={'setting':setting,
             'category':category,
             'page':'home',
             'sliderdata':sliderdata}

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

    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip =request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız iletilmiştir.Bizimle iletişime geçtiğiniz için teşekkür ederiz.")
            return HttpResponseRedirect('/contactus')

    setting=Settings.objects.get(pk=1)
    form=ContactFormu()
    context={'setting':setting,'form':form}

    return render(request,'contactus.html',context)

def category_news(request,id,slug):
    category=Category.objects.all()
    categorydata=Category.objects.get(pk=id)
    news=New.objects.filter(category_id=id)
    context={'news':news,
             'category':category,
             'categorydata':categorydata
             }
    return render(request,'news.html',context)
