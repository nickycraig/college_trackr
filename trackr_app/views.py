from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .models import State, School
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView

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

class SchoolCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        city = request.POST.get("city")
        size = request.POST.get("size")
        public_private = request.POST.get("public_private")
        research_class = request.POST.get("research_class")
        img = request.POST.get("img")
        notes = request.POST.get("notes")
        state = State.objects.get(pk=pk)
        School.objects.create(name=name, city=city, size=size, public_private=public_private, research_class=research_class, img=img, notes=notes, state=state)
        return redirect('region_state_detail', pk=pk)
    
class SchoolDetail(DetailView):
    model = School
    template_name = "school_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SchoolUpdate(UpdateView):
    model = School
    fields = ['name', 'city', 'size', 'public_private', 'research_class', 'img', 'notes', 'state']
    template_name = "school_update.html"
    success_url = "/schools/<int:pk>/"

class SchoolDelete(DeleteView):
    model = School
    template_name = "school_delete_confirmation.html"
    success_url = "/region-state/<int:pk>/"
