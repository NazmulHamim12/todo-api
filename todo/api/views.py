from django.shortcuts import render

from django.http import HttpResponse

from .models import Todo
from .serializer import TodoSerializer

from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.

# Create your views here.




def taskinfo(request):
    com=Todo.objects.all()
    py_data=TodoSerializer(com,many=True)
    json_data=JSONRenderer().render(py_data.data)
    
    return HttpResponse(json_data,content_type='application/json')





@csrf_exempt
def task_add(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        com=TodoSerializer(data=py_data)
        
        
        if com.is_valid():
            com.save()
            res={'msg':'Task Save'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        eror=JSONRenderer().render(com.errors)
        return HttpResponse(eror,content_type='application/json')