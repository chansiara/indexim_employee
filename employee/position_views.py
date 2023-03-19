from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
from cms.views import CoreListView

from .models import Position
from .forms import PositionForm

class PositionUpdate(AjaxUpdateView):
	form_class = PositionForm
	model = Position
	subapp='/position'

	def get_queryset(self):
		return Position.objects.all()

class PositionDelete(AjaxDeleteView):
	model = Position
	subapp='/position'

class PositionDetail(AjaxDetailView):
	model = Position
	subapp='/position'

class PositionList(CoreListView):
	model = Position
	subapp='/position'

	def get_context_data(self,*args,**kwargs):
		context = super(PositionList, self).get_context_data(**kwargs)
		context['module_name'] = 'position'
		context['page_title'] = 'Master Position'
		context['card_title'] = 'PT. INDEXIM COALINDO'
		return context

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.all().order_by('-id')

class PositionCreate(AjaxCreateView):
	model = Position
	form_class = PositionForm
	subapp='/position'