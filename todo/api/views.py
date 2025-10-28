from django.shortcuts import render
from .models import Todo,Sing_up
from .serializer import TodoSerializer,SingupSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.



class Singup(APIView):
    def post(self,request,formate=None):
        data=SingupSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(
                {'Msg':'Your account creat'}
            )
            
        return Response(data.errors)
    
    
    
class LoginView(APIView):
    def post(self,request,format=None):
        email=request.data.get('email')
        password=request.data.get('password')
        
        try:
            user=Sing_up.objects.get(email=email,password=password)
        except Sing_up.DoesNotExist:
            return Response({'msg':"User not found"})
        
        serializer=SingupSerializer(user)
        data=serializer.data
        data.pop('password', None)
        return Response(
            {
                'msg':'User Found',
                'detail':data
                
            }
        )
        
        
        
        
class ProfileView(APIView):
    def get(self,request,pk,format=None):
        try:
            user=Sing_up.objects.get(pk=pk)
        except Sing_up.DoesNotExist:
            return Response({'msg':'user data not found'})
        
        task=Todo.objects.filter(user=user)
        task_data=TodoSerializer(task,many=True)
        serializer=SingupSerializer(user)
        data=serializer.data
        data.pop('password', None)
        
        return Response(
            {
                
                'detail':data,
                'task':task_data.data
            }
        )









class Taskinfo(APIView):
    
    def get(self,request,pk=None,format=None):
        id = pk
        
        
        if id is not None:
            com=Todo.objects.get(pk=id)
            pydata=TodoSerializer(com)
            return Response(pydata.data)
        
        com=Todo.objects.all()
        pydata=TodoSerializer(com,many=True)
        return Response(pydata.data)
            
            
    def post(self,request,format=None):
        
        com=TodoSerializer(data=request.data)
        if com.is_valid():
            com.save()
            return Response({'msg':'Data insert done'})
        
        return Response(com.errors)
    
    def put(self,request,pk,format=None):
        id=pk
        user_data=Todo.objects.get(pk=id)
        exchange_data=TodoSerializer(user_data,data=request.data)
        
        if exchange_data.is_valid():
            exchange_data.save()
            return Response({'msg':'Full data update'})
        
        return Response(exchange_data.errors)
    
    def patch(self,request,pk,format=None):
        id=pk
        user_data=Todo.objects.get(pk=id)
        exchange_data=TodoSerializer(user_data,data=request.data,partial=True)
        
        if exchange_data.is_valid():
            exchange_data.save()
            return Response({'msg':'Partial data update'})
        
        return Response(exchange_data.errors)
    
    
    def delete(self,request,pk,format=None):
        id=pk
        data=Todo.objects.get(pk=id)
        data.delete()
        return Response({'msg':'Delete data'})
            
        

