from django.urls import path
from home.views import shop_info, product_types


urlpatterns = [
    path('shop', shop_info),
    path('types', product_types)
]