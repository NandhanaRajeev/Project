from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeindex, name="homeindex"),
    path('login/', views.login, name="login"),
    path('contacts', views.contacts, name="contacts"),
    path('adminindex', views.adminindex, name="adminindex"),
    path('adminstaff', views.adminstaff, name="adminstaff"),
    path('adminstudent', views.adminstudent, name="adminstudent"),
    path('logout', views.logout, name="logout"),
    
]