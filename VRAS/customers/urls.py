from django.urls import path
from .views import CustomerView, EditCustomerView, DeleteCustomerView


urlpatterns = [
    path('', CustomerView.as_view(), name='customer_list'),
    path('edit/<int:pk>', EditCustomerView.as_view(), name='update_customer'),
    path('<int:pk>/delete', DeleteCustomerView.as_view(), name='delete_customer'),
]