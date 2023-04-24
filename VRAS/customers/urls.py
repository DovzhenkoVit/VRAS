from django.urls import path
from .views import CustomerView, EditCustomerView


urlpatterns = [
    path('', CustomerView.as_view(), name='customer_list'),
    path('edit/<int:pk>', EditCustomerView.as_view(), name='update_customer'),
]