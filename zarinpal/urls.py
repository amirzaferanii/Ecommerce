from django.urls import path
from . import views

app_name = 'zarinpal'

urlpatterns = [
    path('request/payment/<int:pk>', views.SendRequestPayment.as_view(), name='request_payment'),
    path('verify/', views.VerifyView.as_view(), name='verify_payment'),
]