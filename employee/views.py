
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .employee_views import *
from .position_views import *

def page_map(request,module):
	if module == 'employee':
		return EmployeeList.as_view()(request)
	elif module == 'position':
		return PositionList.as_view()(request)
	else:
		return HttpResponse('Not Found')

def index(request):
	context={
		'page_title':'Master Data',
		'card_title':'PT. INDEXIM COALINDO',
		'module_name':None
	}
	return render(request,'employee/index.html',context)

