from django.contrib import admin
from . models import Todo,Sing_up
# Register your models here.
#admin.site.register(Todo)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=['id','user','task','prio']
    
@admin.register(Sing_up)    
class SingAdmin(admin.ModelAdmin):
    list_display=['id','name','email']
