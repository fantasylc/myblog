from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, UserCreationForm, PasswordResetForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
import json


def user_login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect('/itblog/')
    request.session['login_from'] = request.META.get('HTTP_REFERER','/')
    form=LoginForm(request)
    context['form'] = form
    return render(request, 'user_auth/login.html', context)


def user_logout(request):
    if not request.user.is_authenticated():
        raise PermissionDenied

    else:
        logout(request)
        return HttpResponseRedirect('/itblog/')


def register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        errors = []
        form = UserCreationForm(request.POST)
        if form.is_valid():
            title = '欢迎来到superliu.me'
            message = "你好~%s,感谢注册superliu.me!"%(username)+\
                "请牢记您的信息:\n"+\
                "用户名:%s"%(username)+"\n"+\
                "邮箱:%s"%(email)+"\n"
            from_email = ''
            send_mail(title,message,from_email,[email])
            try:
                send_mail(title, message, from_email, [email])
            except Exception as e:
                print(e)
                return HttpResponse("发送邮件失败!\n注册失败", status=500)

            new_user = form.save()
            user = authenticate(username = username,password = password2)
            login(request,user)
            return HttpResponseRedirect('/itblog/')
        else:
            context['form'] = form
            return render(request, 'user_auth/register.html',context)

    form = UserCreationForm()
    context['form'] = form
    return render(request,'user_auth/register.html',context)



