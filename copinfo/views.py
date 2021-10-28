from django.http.response import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import exceptions
from .models import Cop
def info_view(request):
    if request.method=='GET':
        return render(request,'cop/info.html')
    elif request.method=='POST':
        copname=request.POST['copname']
        try:
            cop=Cop.objects.get(copname=copname)
        except Exception as e:
            print('not exist%s'%(e))
            return render(request,'cop/info.html',locals())

        
        return render(request,'cop/info.html',locals())
        
        
        
