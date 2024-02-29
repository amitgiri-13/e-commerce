from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Product,Order

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
    orders = serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "products",
            "orders",
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "product",
            "quantity",
            "order_status",
            "payment_status",
            "order_date",
            "order_address",
            "receiver_name",
            "contact_number",
            "total_price",
        ]
       
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "order_status"
        ]