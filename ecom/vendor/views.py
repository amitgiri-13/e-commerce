from django.shortcuts import render,redirect
from django.views import generic
from store.models import Product,Order
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ProductCreationForm
from store.models import Category,Product

class VendorAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="vendor").exists()

class DashboardView(VendorAccessMixin,LoginRequiredMixin,generic.TemplateView):
    template_name = "vendor/dashboard.html"
    group_required = "vendor"

class ManageProductView(VendorAccessMixin,LoginRequiredMixin,generic.ListView):
    template_name = "vendor/manageproduct.html"
    model = Product
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class ManageOrderView(VendorAccessMixin,LoginRequiredMixin,generic.ListView):
    template_name = "vendor/manageorder.html"
    model = Order
    context_object_name = "order_list"

    def get_queryset(self):
        return Order.objects.filter(product__owner=self.request.user)

# @login_required  
# def add_product(request):
#     category = Category.objects.all()
#     owner = request.user

#     if request.method == "POST":
#         form = ProductCreationForm(request.POST,request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.owner = request.user
#             product.in_stock = True
#             product.save()
#             return redirect("vendor:manageproduct")
        
#     else:
#         form = ProductCreationForm()
    
#     return render(request,"vendor/addproduct.html",{
#         "form":form,
#         })

class AddProductView(VendorAccessMixin,LoginRequiredMixin, generic.TemplateView):
    template_name = "vendor/addproduct.html"

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        form = ProductCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.in_stock = True
            product.save()
            return redirect("vendor:manageproduct")
        return render(request, self.template_name, {"form": form})

@login_required
def delete_product(request,product_id):
    if request.method == "POST":
        product = Product.objects.get(pk=product_id)
        if product.owner == request.user:
            product.delete()
            return redirect("vendor:manageproduct")

    return redirect("vendor:manageproduct")