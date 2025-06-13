"""
URL configuration for aCafineServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import signup, update_phone_number, refresh_token
from dish.views import get_dishes, create_dish, get_specific_dish ,update_dish
from order.views import create_order , seller_orders , mark_order_ready ,get_user_orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', signup, name='signup'),
    path('api/update-phone-number/', update_phone_number, name='update_phone_number'),
    path('api/refresh-token/', refresh_token, name='refresh_token'),
    path('api/get-all-dish/', get_dishes, name='get_all_dish'),
    path('api/create-dish/', create_dish, name='create_dish'),
    path('api/get-specific-dish/',get_specific_dish,name='get_specific_dish'),
    path('api/update-dish/',update_dish,name='update_dish'),
    path('api/create-order/',create_order,name='create_order'),
    path('api/seller-orders/',seller_orders,name='seller_orders'),
    path('api/mark-order-ready/',mark_order_ready,name='mark_order_ready'),
    path('api/get-user-orders/',get_user_orders,name='get_user_orders')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
