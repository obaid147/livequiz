from django.urls import path
from . import views
import uuid


uuid_one = str(uuid.uuid4())
uuid_two = str(uuid.uuid4())
uuid_advanced = 'a_d_' + uuid_one + uuid_two + '_v_c'

urlpatterns = [
    path('{}'.format(uuid_advanced), views.adv_view, name='advanced'),
]
