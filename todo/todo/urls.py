
from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('taskinfo/',views.Taskinfo.as_view()),
    path('taskinfo/<int:pk>',views.Taskinfo.as_view()),
    #path('taskadd/',views.task_add)
]
