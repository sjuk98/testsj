from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *



def logs(request):
    if request.method=='POST':
        fm=log(request.POST)
        if fm.is_valid():
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            a=logNreg.objects.all()
            for i in a:
                if email==i.email and password==i.password:
                    return render(request,'index.html')
            else:
                 return HttpResponse('log error')
       
def all(request):
    v=imagem.objects.all()
    a=[]
    b=[]
    c=[]
    d=[]
    if fm.is_valid():
            id=fm.cleaned_data['id']
            a=serch.objects.all()
    	    for i in v:
		if id==i.id:
        		a.append(i.id)
        		b.append(i.prcs)
        		c.append(i.gstt)
        		d.append(str(z).split("/")[-1])
    			return render(request,'all_item.html',{'w':zip(a,b,c,d)})