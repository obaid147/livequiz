from django.urls import path
from . import views

urlpatterns = [
    path('intermediate', views.inter_view , name='intermediate'),
]
