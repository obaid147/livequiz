from django.urls import path
from . import views


urlpatterns = [
    path('upload', views.user_profile, name='upload'),
]

