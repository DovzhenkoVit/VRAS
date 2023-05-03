from django.urls import path
from .views import RentalAgreementView, AddRentalAgreementView,\
                   EditRentalAgreementView, DeleteRentalAgreementView


urlpatterns = [
    path('', RentalAgreementView.as_view(), name='rental_agreement_list'),
    path('add_rental_agreement/', AddRentalAgreementView.as_view(),name='add_rental_agreement'),
    path('edit/<int:pk>', EditRentalAgreementView.as_view(), name='update_rental_agreement'),
    path('<int:pk>/delete', DeleteRentalAgreementView.as_view(), name='delete_rental_agreement'),
]
