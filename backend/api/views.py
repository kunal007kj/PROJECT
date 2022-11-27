import json
from operator import mod
from urllib import request
from django.http import HttpRequest, HttpResponse, JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import UserProductInlineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def api_home(requst, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = UserProductInlineSerializer(data=request.data)
    if serializer.is_valid():
        print (serializer.data)
        data =  serializer.data
    return Response(data)
