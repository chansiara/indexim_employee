from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
from cms.views import CoreListView

from .models import Employee
from .forms import EmployeeForm

class EmployeeUpdate(AjaxUpdateView):
	form_class = EmployeeForm
	model = Employee
	subapp='/employee'

	def get_queryset(self):
		return Employee.objects.all()

class EmployeeDelete(AjaxDeleteView):
	model = Employee
	subapp='/employee'

class EmployeeDetail(AjaxDetailView):
	model = Employee
	subapp='/employee'

class EmployeeList(CoreListView):
	model = Employee
	subapp='/employee'

	def get_context_data(self,*args,**kwargs):
		context = super(EmployeeList, self).get_context_data(**kwargs)
		context['module_name'] = 'employee'
		context['page_title'] = 'Master Employee'
		context['card_title'] = 'PT. INDEXIM COALINDO'
		return context

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.all().order_by('-id')

class EmployeeCreate(AjaxCreateView):
	model = Employee
	form_class = EmployeeForm
	subapp='/employee'