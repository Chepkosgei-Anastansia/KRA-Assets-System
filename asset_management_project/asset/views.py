from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Asset
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AssetList(ListView):
    model = Asset
    template_name = "asset/instore.html"
    context_object_name = 'assets'

class ProjectCreate(CreateView):
    model = Asset
    fields = ['title','description','lead_developer_id', 'owner']
    success_url = reverse_lazy('projects')  
    template_name = 'base/add_project.html'
    form_class = AssetCreation