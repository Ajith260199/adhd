from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Home.html',views.Home,name='Home'),
    path('test.html',views.test,name='test'),
    path('test',views.adulttest,name='adulttest'),
    path('child-test.html',views.childtest,name='childtest'),
    path('contact-us.html',views.contactus,name='contactus'),
    path('userdetails',views.adultdetails,name='adultdetails')

]