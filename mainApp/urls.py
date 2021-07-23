from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainApp-index'),
    path('about/', views.aboutus, name='mainApp-about'),
    path('contact/', views.contactus, name='mainApp-contact'),
    path('sellcar/', views.sellcar, name='mainApp-sellcar'),
    path('adminlogin/', views.adminlogin, name='mainApp-adminlogin'),
    path('adminlogout/',views.adminlogout, name='mainApp-adminlogout'),
    path('adminmanage/',views.adminmanage, name='mainApp-adminmanagepage'),
    path('adminviewcars/', views.adminviewcars, name='mainApp-adminviewcars'),
    path('adminviewmessages/', views.adminviewmessages, name='mainApp-adminviewmessages'),
    path(r'^<int:id>cardetails/', views.cardetails, name='mainApp-cardetails'),
    path(r'^<int:id>delcar/', views.deletecar, name='mainApp-delcar'),
    path(r'^<int:id>delcustcar/', views.deletecustcar, name='mainApp-delcustcar'),
]