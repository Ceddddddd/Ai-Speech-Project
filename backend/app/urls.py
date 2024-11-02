from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page, name='main'),
    path('home/',views.home, name='home'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('registerForm/',views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('transcript/summarize/', views.summarize, name='summary'),  
    path('question/', views.question, name='question') ,
    path('translate/', views.translate, name='translate') 
]
