from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render,redirect
from .models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@api_view(["GET","POST"])
#@login_required(login_url="/login")
def todo_lst(request):
        
        if request.method == "GET":
                                todos=Todo.objects.all()
                                serializer=TodoSerializer(todos,many=True)
                                return Response(serializer.data)
        
        elif request.method == "POST":
                        serializer = TodoSerializer(data=request.data)
                        if serializer.is_valid():
                                serializer.save()
                                return Response(serializer.data,status=status.HTTP_201_CREATED)
                        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
@api_view(["GET","PATCH","PUT","DELETE"])           
def todo_detail(request,pk):
            todo=get_object_or_404(Todo,id=pk)
            if request.method=="GET":
                                serializer=TodoSerializer(todo)
                                return Response(serializer.data)
                                
            elif request.method=='PUT':
                                serializer=TodoSerializer(todo,data=request.data)
                                if serializer.is_valid():
                                                        serializer.save()
                                                        return Response(serializer.data)
                                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                                todo.delete()
                                return Response(status=status.HTTP_204_NO_CONTENT)




#login
"""
def login_pg(request):
    if request.method=="POST": 
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid name')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect("http://localhost:5173")

    return render(request,"login.html")

#register
def register_pg(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'username already taken')
            return redirect('/register/')

        user=User.objects.create(

            username=username

        )
        user.set_password(password)
        user.save()

        messages.info(request,'account created please login!')

        return redirect("/register/")

    else:
        # Handle the GET request to display the registration form
        return render(request, 'register.html')
    

#logout
def logout_pg(request):
    logout(request)
    return redirect('/logout/')"""