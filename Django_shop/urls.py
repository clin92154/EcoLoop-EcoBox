"""Django_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include  # 引用include函式
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')) ,#新增應用程式的網址
    path('cart/', include('cart.urls')), #新增應用程式的網址
    path('orders/', include('orders.urls')), #新增應用程式的網址
    path('payment/', include('payment.urls')), #新增應用程式的網址
    path('ecobot/', include('ecobot.urls')) #包含應用程式的網址
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

