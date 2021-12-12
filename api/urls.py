from django.urls import path
from . import views


urlpatterns = [
    path('member', views.memberApi),
    path('member/<int:id>', views.memberApi),
]
