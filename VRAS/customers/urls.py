from django.urls import path
from .views import CustomerView, AddCustomerView, EditCustomerView, DeleteCustomerView


urlpatterns = [
    path('', CustomerView.as_view(), name='customer_list'),
    path('add_customer/', AddCustomerView.as_view(), name='add_customer'),
    path('edit/<int:pk>', EditCustomerView.as_view(), name='update_customer'),
    path('<int:pk>/delete', DeleteCustomerView.as_view(), name='delete_customer'),
]
