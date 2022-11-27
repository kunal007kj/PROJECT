from math import prod
from urllib.error import URLError
from urllib.parse import urlparse
from django.urls import  path
from rest_framework.authtoken.views import obtain_auth_token

from products.views import ProductDetailAPIView
from . import views


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home),  #localhost:8000/api/ 
    #path('api/products', )

]