from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.db import models

from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import viewsets


from store.serializers import ProductSerializer,UserSerializer,OrderSerializer,OrderStatusSerializer
from store.models import Product,Order
from store.permissions import IsOwnerORReadOnly,IsVendorORReadOnly,IsOrderBuyerOrReadOnly
@api_view(["GET"])
def api_home(request):
    return Response({
        "users" : reverse("users",request=request),
        "proudcts" : reverse("products",request=request),
    })

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerORReadOnly,IsVendorORReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes =[permissions.IsAdminUser]

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOrderBuyerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return OrderStatusSerializer
        return OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            models.Q(buyer=self.request.user) |
            models.Q(product__owner=self.request.user)
        )
    
    def perform_create(self,serializer):
        if self.request.method == "POST":
            serializer.save(buyer = self.request.user,order_status= "CR",payment_status=False)

    def perform_update(self,serializer):
        if self.request.method == "PATCH" and serializer.instance.order_status == "CR":

            if  self.request.data["order_status"]=="CN" and self.request.user == serializer.instance.buyer:
                serializer.save(order_status="CN")

            if self.request.data["order_status"]=="DP" and self.request.user == serializer.instance.seller:
                serializer.save(order_status="DP")
