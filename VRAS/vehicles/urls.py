from django.urls import path
from .views import VehicleView


urlpatterns = [
    path('', VehicleView.as_view(), name='vehicle_list'),
    
]