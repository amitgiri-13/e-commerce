from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url = True)
    
    class Meta:
        model = Product
        fields = [
            "category",
            "product",
            "description",
            "price",
            "image",
            "created_at",
            "in_stock",
        ]
 
class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "products",
        ]