from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
   path('',views.index,name='home'),
   path('about',views.about,name='about'),
   path('service1',views.service1,name='service1'),
   path('contact',views.contact,name='contact'),
     path('login', views.loginuser,name="login"),
    path('logout', views.logoutuser,name="logout")
]
