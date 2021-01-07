from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import uuid


uuid_one = str(uuid.uuid4())
uuid_two = str(uuid.uuid4())
uuid_start = 'q_u_' + uuid_one + uuid_two + '_i_z'

urlpatterns = [
    path('', views.index, name='index'),
    path(f'{uuid_start}', views.start, name='start'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout_req, name='logout'),
    path('login/', views.login_req, name='login'),

    # reset password urls
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='regestration/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='regestration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='regestration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='regestration/password_reset_complete.html'), name='password_reset_complete'),

]
