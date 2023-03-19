from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='indexim_employee'
urlpatterns = [
    path('employee/',include('employee.urls',namespace='employee')),

   path('',index, name='index'),
   path('admin/', admin.site.urls),
]
