from django.urls import path

from .views import RatesAPIView


urlpatterns = [
    path('rates/', RatesAPIView.as_view()),
]
