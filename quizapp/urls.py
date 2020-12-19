from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('start', views.start, name='start'),
]
