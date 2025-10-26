from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


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
            
        

