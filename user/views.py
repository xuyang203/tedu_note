from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import exceptions
from .models import User
import hashlib
# Create your views here.

def reg_view(request):
    if request.method =='GET':
        
        return render(request,'user/reg.html')
    elif request.method =='POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if password_1 !=password_2:
            return HttpResponse('两次密码不一致')
        
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')
        try:
            user = User.objects.create(username=username,password=password_m)
        except Exception as e:
            print('--create user error %s'%(e)) 
            return HttpResponse(' 用户已注册')
        request.session['username'] = username
        request.session['uid'] = user.id

        return HttpResponseRedirect('/home')


def log_view(request):
    if request.method =='GET':
        if request.session.get('username') and request.session.get('uid'):
            #return HttpResponse('已登陆')
            return HttpResponseRedirect('/home')

        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username']=c_username
            request.session['uid']=c_uid
            #return HttpResponse('已登陆')
            return HttpResponseRedirect('/home')

        return render(request,'user/log.html')
    elif request.method=='POST':
        username = request.POST['username']
        password  = request.POST['password']
    try:
         user= User.objects.get(username=username)
    except Exception as e:
        print('--login user error %s'%(e))
        return HttpResponse('用户名或密码错误')

    m=hashlib.md5()
    m.update(password.encode())
    password_m = m.hexdigest()
    if user.password==password_m:
        request.session['username']=username
        request.session['uid']=user.id
#       resp = HttpResponse('登录成功')
        resp =  HttpResponseRedirect('/home')


        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid',user.id,3600*24*3)
        return resp
        

    else:
        return HttpResponse('用户名或密码错误')


def logout_view(request):
    '''
    response = HttpResponseRedirect('/index')     #改成重定向等都可以
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response
    '''
    del request.session['username']

   
    response = HttpResponseRedirect('/index')
    response.delete_cookie('username')
    return response
