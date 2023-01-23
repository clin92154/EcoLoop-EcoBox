from django.urls import path ,  re_path
from . import views  #引用這個資料夾中的views檔案
app_name = 'shop'
urlpatterns = [
    re_path(r'^$', views.product_list,
        name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail')
    ]