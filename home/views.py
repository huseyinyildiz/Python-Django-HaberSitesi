import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Settings, ContactFormu, ContactFormMessage, UserProfile, FAQ
from home.forms import SearchForm, RegisterForm
from news.models import New, Category, Images, Comment


def index(request):
    setting=Settings.objects.get(pk=1)
    sliderdata =New.objects.all().order_by('?')[:4]
    category=Category.objects.all()
    daily=New.objects.all().order_by('?')[:6]
    recommend=New.objects.all().order_by('?')[:3]
    context={'setting':setting,
             'category':category,
             'page':'home',
             'sliderdata':sliderdata,
             'daily':daily,
             'recommend':recommend}

    return render(request,'index.html',context)

def aboutus(request):
    setting=Settings.objects.get(pk=1)
    category = Category.objects.all()
    context={'setting':setting,'page':'aboutus','category':category}

    return render(request,'aboutus.html',context)

def references(request):
    setting=Settings.objects.get(pk=1)
    category = Category.objects.all()
    context={'setting':setting,'page':'references','category':category}

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
    category = Category.objects.all()
    form=ContactFormu()
    context={'setting':setting,'form':form,'category':category}

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

def new_detail(request,id,slug):
    category=Category.objects.all()
    new = New.objects.get(pk=id)
    images=Images.objects.filter(news_id=id)
    comments = Comment.objects.filter(new_id=id,status='True')
    context={'category':category,
             'new':new,
             'images':images,
             'comments':comments}
    return render(request,'new_detail.html',context)

def new_search(request):
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query=form.cleaned_data['query']
            new=New.objects.filter(title__icontains=query)

            context = {'new':new,
                       'category':category,}
            return render(request,'new_search.html',context)
        return HttpResponseRedirect('/')

def new_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        new = New.objects.filter(title__icontains=q)
        results = []
        for rs in new:
            new_json = {}
            new_json = rs.title
            results.append(new_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.error(request,'Kullanıcı adı veya şifre yanlış.')
            return HttpResponseRedirect('/login/')
    category=Category.objects.all()
    context={'category':category}
    return render(request,'login.html',context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            return HttpResponseRedirect('/')
    form = RegisterForm()
    category = Category.objects.all()
    context = {'category':category,
               'form':form,}
    return render(request,'register.html',context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all()
    context = {
        'category':category,
        'faq':faq
    }
    return render(request,'faq.html',context)