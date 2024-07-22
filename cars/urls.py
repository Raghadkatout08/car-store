from django.urls import path
from .views import HomePageView, CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('car_list/', CarListView.as_view(), name='car_list'),
    path('car_detail/<int:pk>/', CarDetailView.as_view(), name= 'car_detail'),
    path('car_create/', CarCreateView.as_view(), name='car_create'),
    path('car_update/<int:pk>', CarUpdateView.as_view(), name='car_update'),
    path('car_delete/<int:pk>', CarDeleteView.as_view(), name='car_delete'),

]