from django.urls import path
from demo1 import views

app_name='demo1'

urlpatterns=[
    path('index1/',views.index1,name="index1"),
    path('index2/',views.index2,name="index2"),
    path('index3/<data>',views.index3,name="index3"),
    path('index4/<a>/<b>/',views.index4,name="index4"),
]