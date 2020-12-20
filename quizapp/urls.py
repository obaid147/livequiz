from django.urls import path
from . import views


urlpatterns = [
	path('', views.start, name='start'),
	path('index', views.index, name='index'),
	path('login', views.login, name='login'),

]
