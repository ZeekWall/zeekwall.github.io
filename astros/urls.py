from django.urls import path
from astros import views

urlpatterns = [
    path('', views.astros, name='astros'),
]