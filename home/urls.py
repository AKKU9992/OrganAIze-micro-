from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
   path('',views.index,name='home'),
   path('about',views.about,name='about'),
  #  path('service1',views.service1,name='service1'),
    path('service2',views.service2,name='service2'),
   path('contact',views.contact,name='contact'),
     path('login', views.loginuser,name="login"),
    path('logout', views.logoutuser,name="logout"),
       path('month/', views.month, name='month'),
    path('week/', views.week, name='week'),
    path('add/', views.add, name='add'), #Add URL
    path('addmonth/', views.addmonth, name='addmonth'),
    path('addweek/', views.addweek, name='addweek'),
    path('delete/<int:todo_id>/', views.deleteItem, name='delete'),
    path('deleteweek/<int:todoweek_id>/', views.deleteweek, name='deleteweek'),
    path('deletemonth/<int:todomonth_id>/', views.deletemonth, name='deletemonth'),
    # path('task/<int:task_id>/', views.task_detail, name='task_detail')
]
