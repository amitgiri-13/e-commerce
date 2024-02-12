from django.shortcuts import render
from django.views import generic
from store.models import Product,Order

class DashboardView(generic.TemplateView):
    template_name = "vendor/dashboard.html"

class ManageProductView(generic.ListView):
    template_name = "vendor/manageproduct.html"
    model = Product
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class ManageOrderView(generic.ListView):
    template_name = "vendor/manageorder.html"
    model = Order
    context_object_name = "order_list"

    def get_queryset(self):
        return Order.objects.filter(product__owner=self.request.user)
    