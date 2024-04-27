from django.urls import path
from productdescription.views import prices, shop_name


urlpatterns = [
    path('name', shop_name),
    path('prices', prices)
]