import imp
from multiprocessing.spawn import import_main_path
from rest_framework import viewsets

from .models import Product
from .serializers import UserProductInlineSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get --> list --> queryset
    get --> retrive --> product Instance detail view
    post --> create --> new Instance
    put -->  update 
    patch -->  Partial update
    delete --> destroy
    """
    queryset = Product.objects.all()
    serializer_class  = UserProductInlineSerializer
    lookup_field = 'pk' #default