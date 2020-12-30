from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.start, name='start'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout_req, name='logout'),
    path('login/', views.login_req, name='login'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
