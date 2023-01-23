from . import views
from django.urls import path ,  re_path
app_name = 'orders'

urlpatterns = [
        re_path(r'^create/$',
            views.order_create,
            name='order_create'),
]