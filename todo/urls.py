from django.urls import path
from . import views
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('',views.todo_lst,name="l"),
    #path('login/',views.login_pg,name="login"),
    path('todos', views.todo_lst),
    #path('logout/',views.logout_pg,name="logout_pg"),
    path("todos/<int:pk>",views.todo_detail),
    #path('register/',views.register_pg,name='register_pg'),
    
]





