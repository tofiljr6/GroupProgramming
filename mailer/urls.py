from django.urls import path
from .views import sendNewsletter, sendReceipt

urlpatterns = [
    path('mailer/', sendNewsletter),
    path('receipt/', sendReceipt),
]