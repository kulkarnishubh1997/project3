"""pro3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pro3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo1/',include('demo1.urls')),
    path('index/',views.index,name="index"),
    path('home/<data>',views.home,name="home"),
    path('demo1/<data>/',views.demo1,name="demo1"),
    path('login/<data>/',views.login,name="login"),
    path('demo2/',views.demo2,name="demo2"),
    path('demo3/',views.demo3,name="demo3"),

    path('file1/',views.file1,name="file1"),
    path('file2/',views.file2,name="file2"),
    path('file3/<data>/',views.file3,name="file3"),


]
