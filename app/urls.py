from django.urls import path
from . import views
urlpatterns = [
     path('',views.index,name='index'),   
     path('login',views.loginUser,name='login'),   
     path('signup',views.signupUser,name='signup'),   
     path('dashboard',views.dashboard,name='dashboard'),   
     path('logout',views.logoutUser,name='logout'),   
 ]
 