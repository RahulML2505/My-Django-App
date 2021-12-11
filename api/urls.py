from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contactApi),
    path('contact/<int:id>', views.contactApi),
]
