from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars_object'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['buyer_id', 'model', 'brand', 'price', 'is_bought', 'buy_time']

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = '__all__'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_list')