from django.urls import path
from . import views

urlpatterns = [
    path('advanced', views.adv_view, name='advanced'),
]
