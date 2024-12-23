from django.urls import path
from .views import GenerateQR

urlpatterns = [
    path("GenerateQR/",GenerateQR.as_view())
]
