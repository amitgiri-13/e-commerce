from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets


from store.serializers import ProductSerializer,UserSerializer
from store.models import Product
from store.permissions import IsOwnerORReadOnly,IsVendorORReadOnly

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
