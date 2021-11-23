from django.http.response import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import exceptions
from .models import Fin
def data_view(request):
    if request.method=='GET':
        return render(request,'fin/data.html')
    elif request.method=='POST':
        copname=request.POST['copname']
        a=copname
        try:
            fin=Fin.objects.get(copname=copname)
        except Exception as e:
            print('not exist%s'%(e))
            return render(request,'fin/data.html',locals())

        
        return render(request,'fin/data.html',locals())
        
        
        
