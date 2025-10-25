from rest_framework import serializers
from . models import Todo



class TodoSerializer(serializers.Serializer):
    task=serializers.CharField(max_length=100)
    
    
    def create(self, validated_data):
        return Todo.objects.create(**validated_data)