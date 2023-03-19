from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'employee'
urlpatterns =[
	path('employee/delete/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete'),
	path('employee/update/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
	path('employee/create/', EmployeeCreate.as_view(), name='employee-create'),
	path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee-detail'),

	path('position/delete/<int:pk>/', PositionDelete.as_view(), name='position-delete'),
	path('position/update/<int:pk>/', PositionUpdate.as_view(), name='position-update'),
	path('position/create/', PositionCreate.as_view(), name='position-create'),
	path('position/<int:pk>', PositionDetail.as_view(), name='position-detail'),

	path('<str:module>/', page_map, name='pages'),
	path('', index, name='index'),
]