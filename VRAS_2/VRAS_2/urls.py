from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('rental_agreements.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('customers/', include('customers.urls')),
]
