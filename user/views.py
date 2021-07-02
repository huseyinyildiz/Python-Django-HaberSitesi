from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile , Settings
from news.models import Category, Comment, New
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import ContentForm

@login_required(login_url='/login') # Check login
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category':category,
               'profile':profile}
    return render(request,'user_profile.html',context)

@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES , instance = request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Hesabınız güncellendi')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request,'Profiliniz güncellenemedi.' +str(user_form.errors) +str(profile_form.errors))
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login') # Check login
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Şifreniz başarıyla değiştirildi.')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request,'Lütfen boşlukları doğru doldurunuz.' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request,'change_password.html', {
            'form':form ,'category':category
        })

@login_required(login_url='/login') # Check login
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'comments':comments
    }
    return render(request,'user_comments.html',context)

@login_required(login_url='/login') # Check login
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id = id,user_id=current_user.id).delete()
    messages.success(request,'Silindi.')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login') # Check login
def contents(request):
    category = Category.objects.all()
    current_user = request.user
    contents = New.objects.filter(user_id = current_user.id)
    form = ContentForm()
    context = {
        'category':category,
        'contents':contents
    }
    return render(request,'user_contents.html',context)

@login_required(login_url='/login') # Check login
def addcontent(request):
    if request.method=='POST':
        form=ContentForm(request.POST,request.FILES)
        if form.is_valid():
            current_user=request.user
            data=New()
            data.user_id=current_user.id
            data.title=form.cleaned_data['title']
            data.keywords=form.cleaned_data['keywords']
            data.description=form.cleaned_data['description']
            data.image=form.cleaned_data['image']
            data.category=form.cleaned_data['category']
            data.slug=form.cleaned_data['slug']
            data.detail=form.cleaned_data['detail']
            data.status='False'
            data.save()
            messages.success(request,'Haberiniz eklendi.')
            return  HttpResponseRedirect('/user/contents')
        else:
            messages.error(request,'Hata :' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        category= Category.objects.all()
        form=ContentForm()
        context={
            'category':category,
            'form':form,
        }
        return render(request,'user_addcontent.html',context)

@login_required(login_url='/login') # Check login
def contentedit(request,id):
    content=New.objects.get(id=id)
    if request.method=='POST':
        form=ContentForm(request.POST,request.FILES,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request,'Haber başarıyla güncellendi.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request,'Hatam Error:'+ str(form.errors))
            return HttpResponseRedirect('/user/contentedit'+str(id))
    else:
        category=Category.objects.all()

        form=ContentForm(instance=content)
        context={
            'category':category,
            'form':form
        }
        return render(request,'user_addcontent.html',context)

@login_required(login_url='/login') # Check login
def contentdelete(request,id) :
    current_user=request.user
    New.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request,'Content Deletedd..')
    return HttpResponseRedirect('/user/contents')