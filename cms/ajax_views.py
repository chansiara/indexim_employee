from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .views import (
    CoreListView, CoreDetailView, CoreCreateView,
    CoreUpdateView, CoreDeleteView
)
from .mixins import (
    AjaxCreateMixin,AjaxUpdateMixin,AjaxDetailMixin,AjaxDeleteMixin,AjaxSoftDeleteMixin,
    PassRequestToFormViewMixin, ModelMixin
)



class AjaxCreateView(AjaxCreateMixin, PassRequestToFormViewMixin,
                     ModelMixin, CreateView):
    template = ''
    ajax_partial = ''
    ajax_list_partial = ''
    model_name = ''
    app = ''
    subapp=''
    def dispatch(self, *args, **kwargs):
        self.template = 'form'
        self.app = self.model._meta.app_label+'{}'.format(self.subapp)
        self.model_name = self.model.__name__.lower()
        self.ajax_partial = '{}/partials/{}_form.html'.format(self.app,self.model_name)
        self.ajax_list_partial = '{}/partials/{}_list.html'.format(self.app,self.model_name)
        return super().dispatch(*args, **kwargs)

class AjaxUpdateView(AjaxUpdateMixin, PassRequestToFormViewMixin,
                     ModelMixin, UpdateView):
    template = ''
    ajax_partial = ''
    ajax_list_partial = ''
    model_name = ''
    app = ''
    subapp=''
    def dispatch(self, *args, **kwargs):
        self.template = 'form'
        self.app = self.model._meta.app_label+'{}'.format(self.subapp)
        self.model_name = self.model.__name__.lower()
        self.ajax_partial = '{}/partials/{}_form.html'.format(self.app,self.model_name)
        self.ajax_list_partial = '{}/partials/{}_list.html'.format(self.app,self.model_name)
        return super().dispatch(*args, **kwargs)

class AjaxDetailView(AjaxDetailMixin, ModelMixin, DetailView):
    template = ''
    ajax_partial = ''
    ajax_list_partial = ''
    model_name = ''
    app = ''
    subapp=''
    def dispatch(self, *args, **kwargs):
        self.template = 'detail'
        self.app = self.model._meta.app_label+'{}'.format(self.subapp)
        self.model_name = self.model.__name__.lower()
        self.ajax_partial = '{}/partials/{}_detail.html'.format(self.app,self.model_name)
        return super().dispatch(*args, **kwargs)


class AjaxSoftDeleteView(AjaxSoftDeleteMixin, PassRequestToFormViewMixin,
                     ModelMixin, DeleteView):
    template = ''
    ajax_partial = ''
    ajax_list_partial = ''
    model_name = ''
    app = ''
    subapp=''
    def dispatch(self, *args, **kwargs):
        self.template = 'confirm_delete'
        self.app = self.model._meta.app_label+'{}'.format(self.subapp)
        self.model_name = self.model.__name__.lower()
        self.ajax_partial = '{}/partials/{}_confirm_delete.html'.format(self.app,self.model_name)
        self.ajax_list_partial = '{}/partials/{}_list.html'.format(self.app,self.model_name)
        return super().dispatch(*args, **kwargs)

class AjaxDeleteView(AjaxDeleteMixin, PassRequestToFormViewMixin,
                     ModelMixin, DeleteView):
    template = ''
    ajax_partial = ''
    ajax_list_partial = ''
    model_name = ''
    app = ''
    subapp=''
    def dispatch(self, *args, **kwargs):
        self.template = 'confirm_delete'
        self.app = self.model._meta.app_label+'{}'.format(self.subapp)
        self.model_name = self.model.__name__.lower()
        self.ajax_partial = '{}/partials/{}_confirm_delete.html'.format(self.app,self.model_name)
        self.ajax_list_partial = '{}/partials/{}_list.html'.format(self.app,self.model_name)
        return super().dispatch(*args, **kwargs)
