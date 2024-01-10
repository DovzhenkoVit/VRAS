# rental_agreements/urls.py
from django.urls import path
from .views import (
    RentalAgreementListView,RentalAgreementDetailView,
    RentalAgreementCreateView,RentalAgreementUpdateView,ReceiptView
)

urlpatterns = [
    path('rental-agreements/', RentalAgreementListView.as_view(), name='rental-agreement-list'),
    path('rental-agreements/<int:pk>/', RentalAgreementDetailView.as_view(), name='rental-agreement-detail'),
    path('rental-agreements/add/', RentalAgreementCreateView.as_view(), name='rental-agreement-add'),
    path('rental-agreements/<int:pk>/edit/', RentalAgreementUpdateView.as_view(), name='rental-agreement-edit'),
    path('rental-agreements/<int:pk>/receipt/', ReceiptView.as_view(), name='receipt'),
]
