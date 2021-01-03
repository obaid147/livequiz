from django.urls import path
from . import views
import uuid


uuid_one = str(uuid.uuid4())
uuid_two = str(uuid.uuid4())
uuid_intermediate = 'i_n_' + uuid_one + uuid_two + '_t_r'

urlpatterns = [
    path(f'{uuid_intermediate}', views.inter_view, name='intermediate'),
]
