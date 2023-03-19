from django import forms
from django.forms import ModelForm
from .models import Employee,Position

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields =(
			'name',
			'gender',
			'position',
			'address',
			'religion',
			'marital',
			'email',
			'phone',
		)
		
	def __init__(self, *args, **kwargs):
		request = kwargs.pop('request')
		super().__init__(*args, **kwargs)
		self.fields['position']=forms.ModelChoiceField(queryset=Position.objects.all())

class PositionForm(forms.ModelForm):
	class Meta:
		model = Position
		fields =(
			'name',
			'base_salary',
			'transport',
			'family_incentive',
			'bpjs_cut',
		)
		
	def __init__(self, *args, **kwargs):
		request = kwargs.pop('request')
		super().__init__(*args, **kwargs)