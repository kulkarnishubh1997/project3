from django.shortcuts import render

def index(request):
    return render(request,'index.html',context={'data':'shubh'})

def home(request,data):
    return render(request,'index.html',context={'data':data,'li':[10,20,30],'dt':{'a':60,'b':80}})

def demo1(request,data):
    return render(request,'demo1.html',{'li':[10,100,20]})

def login(request,data):
    return render(request,'demo.html',{'res':data})

def demo2(request):
    data=[10,20,30,40,50,60,70,80]
    return render(request,'demo2.html',{'res':data})

def demo3(request):
    d=['hello','world','i','love','india']
    e="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quasi ad sed modi totam, 
        architecto sequi optio, quidem aperiam officia 
        veniam animi atque iusto molestias ullam voluptatum nemo repudiandae itaque?"""
    return render(request,'demo3.html',{'a':10,'b':'smillar','c':[10,20],'d':d,'e':e})

def file1(request):
    return render(request,'file1.html')

def file2(request):
    return render(request,'file2.html')

def file3(request,data):
    return render(request,'file3.html',{'new':data})



