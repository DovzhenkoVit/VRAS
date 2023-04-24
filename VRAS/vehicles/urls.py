from django.urls import path
from .views import VehicleView, EditVehicleView


urlpatterns = [
    path('', VehicleView.as_view(), name='vehicle_list'),
    path('edit/<int:pk>', EditVehicleView.as_view(), name='update_vehicle'),
]
