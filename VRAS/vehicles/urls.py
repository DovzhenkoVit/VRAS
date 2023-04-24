from django.urls import path
from .views import VehicleView, EditVehicleView, DeleteVehicleView


urlpatterns = [
    path('', VehicleView.as_view(), name='vehicle_list'),
    path('edit/<int:pk>', EditVehicleView.as_view(), name='update_vehicle'),
    path('<int:pk>/delete', DeleteVehicleView.as_view(), name='delete_vehicle'),
]
