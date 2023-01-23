from django.conf.urls import re_path
from . import views
app_name='payment'
urlpatterns = [
    re_path(r'^done/$', views.payment_done
        , name='done'),
]