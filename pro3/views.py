from django.shortcuts import render

def index(request):
    return render(request,'index.html',context={'data':'shubh'})

def home(request,data):
    return render(request,'index.html',context={'data':data,'li':[10,20,30],'dt':{'a':60,'b':80}})