import email
from itertools import product
from msilib.schema import ServiceInstall
from turtle import st
from django.http import Http404
from rest_framework import  generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from api.authentication import  TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

from .models import Product
#from ..api.permissions import IsStaffEditorPermission
from .serializers import UserProductInlineSerializer



class ProductListCreatAPIVIEW(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = UserProductInlineSerializer
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission ]                                       # .Attributes  --> Permissions

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        email = serializer.validated_data.pop('email')
        print(serializer.validated_data)
        title = serializer.validated.data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        return super().perform_create(serializer)
       
       
        #send  a  django signal
product_list_create_view = ProductListCreatAPIVIEW.as_view()


class ProductMixinView(
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = UserProductInlineSerializer
    lookup_field = 'pk'
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission ]                                              # .Attributes  --> Permissions
    
    def get(self, request, *args, **kwargs ): 
        print(args, kwargs)
        pk = (args, kwargs)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs ):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)       
        title = serializer.validated.data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is single view doing cool stufff"
        serializer.save(content=content)



product_mixin_view = ProductMixinView.as_view()
 
class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):                                                                                              # DETAIL API VIEW                                                                                                                                                                                    
      serializer_class = UserProductInlineSerializer
      #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission ]                                             # .Attributes  --> Permissions
      lookup_field = 'pk'
    
product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):                                                                                                # UPDATEAPIVIEW
    queryset = Product.objects.all()
    serializer_class = UserProductInlineSerializer
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission ]                                               # .Attributes  --> Permissions
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        #return super().perform_update(serializer)(s)
    
product_Update_view = ProductUpdateAPIView.as_view()                                                                        # DESTROYAPIVIEW

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = UserProductInlineSerializer
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission ]                                               # .Attributes  --> Permissions
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        #instance = serializer.save()
        return super().perform_destroy(instance)()
    
product_destroy_view = ProductUpdateAPIView.as_view()

#class ProductListAPIView(generics.ListAPIView):
#    """ NOT GONNA USE THIS METHOD
#    Instead using (ListCreatAPIVIEW) """

#    serializer_class = ProductSerializer
#    lookup_field = 'pk'

    
#product_List_view = ProductListAPIView.as_view()



@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method        # PUT --> update # DESTROY --> delete

    if method == "GET":
        if pk is not None:
            #detail view
            queryset = Product.objects.filter(pk=pk)
            # obj =get_object_or_404(Product, pk=pk)
            if not queryset.exists():
                raise Http404
            return Response()

        
        #url_args??
        #get Request --> detail view
        #list view
        queryset = Product.objects.all()
        data = UserProductInlineSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = UserProductInlineSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
            title = serializer.validated.data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
