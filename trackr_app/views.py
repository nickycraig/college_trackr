from django.shortcuts import render
from django.views import View
from .models import State
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class RegionStateList(TemplateView):
    template_name = "region_state_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = State.objects.all()
        return context
 
class RegionStateDetail(DetailView):
    model = State
    template_name = "region_state_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


