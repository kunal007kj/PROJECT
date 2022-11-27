from audioop import reverse
from dataclasses import field
import email
from unicodedata import lookup
from wsgiref import validate
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

from django.contrib.auth import get_user_model

User = get_user_model()

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
            read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    this_is_not_real = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    get_my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name= 'product-detail',
            lookup_field='pk'
    )
    email = serializers.EmailField(write_only= True)
    
class Meta:                                                    #can be changed 
        model = Product
        fields = [
            'url',
            'edit_url',
            'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]         
         
    #def create(self, validated_data):
    #    return Product.objects.create(**validated_data)
    #    email = validated_data.pop('email')
    #    obj = super(self).create(validated_data)
    #    print(email, obj)
    #    return obj        
    #
    #def update(self, instance, validate_data):
    #    instance.title = validate_data.get('title')
    #    return super(self).update(instance, validate_data)

def get_edit_url(self, obj):
    # return f"/api/v2/products/{obj.pk}/"
    request = self.context.get('request') #self.request
    if request is None:
        return None
    return reverse("product-edit", kwargs= {"pk": obj.pk}, request=request)

def get_my_discount(self, obj):
     try:
         return obj.get_discount()
     except:
         return None    