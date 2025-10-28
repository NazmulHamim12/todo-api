from rest_framework import serializers
from . models import Todo,Sing_up



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','user','task','prio']
        
        
        
class SingupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sing_up
        fields=['id','name','email','password']
        
        
        
