from django.shortcuts import render,redirect
from django.views import generic
from store.models import Product,Order,Profile
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils import timezone


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ProductCreationForm
from store.models import Category,Product,Order

class VendorAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="vendor").exists()

class DashboardView(VendorAccessMixin,LoginRequiredMixin,generic.TemplateView):
    template_name = "vendor/dashboard.html"
    
    def  get_queryset(self):
        return Order.objects.filter(product__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_orders"] =  self.get_queryset().count()
        context["total_returned_orders"] = self.get_queryset().filter(order_status="RTV").count()
        context["total_delivered_orders"] = self.get_queryset().filter(order_status="DV").count()
        context["orders_in_process"] = self.get_queryset().filter(order_status="DP").count()
        context["order_value"] = sum(order.total_price for order in self.get_queryset())
        context["returned_value"] = sum(order.total_price for order in self.get_queryset().filter(order_status="RTV"))
        context["delivered_value"] = sum(order.total_price for order in self.get_queryset().filter(order_status="DV"))
        context["pending_value"] = sum(order.total_price for order in self.get_queryset().filter(order_status="DP"))


        context["today_order_count"] = self.get_queryset().filter(order_date__date = timezone.now().date()).count()
        context["today_order_value"] = sum(order.total_price for order in self.get_queryset().filter(order_date__date=timezone.now().date()))
        return context
    
    

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

class EditProductView(VendorAccessMixin,LoginRequiredMixin,generic.TemplateView):
    template_name = "vendor/editproduct.html"

    def get(self,request,*args,**kwargs):
        product_id = kwargs.get("product_id")
        product = Product.objects.get(pk=product_id)
        form = ProductCreationForm(instance=product)
        
        return render(request,self.template_name,{"form":form})

    def post(self,request,*args,**kwargs):
        product_id = kwargs.get("product_id")
        product = Product.objects.get(pk=product_id)
        form = ProductCreationForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.in_stock = request.POST.get("in_stock")
            product.save()
            return redirect("vendor:manageproduct")
        
        return render(request,self.template_name,{"form":form})

class ShippingView(VendorAccessMixin,LoginRequiredMixin,generic.DetailView):
    model = Order
    template_name = "vendor/shipping.html"
    context_object_name = "order" 

class SettingView(VendorAccessMixin,LoginRequiredMixin,generic.DetailView):
    template_name = "vendor/setting.html"
    model = Profile
    context_object_name = "profile"
    
    def get_object(self):
        return self.request.user.profile



@login_required
def delete_product(request,product_id):
    if request.method == "POST":
        product = Product.objects.get(pk=product_id)
        if product.owner == request.user:
            product.delete()
            return redirect("vendor:manageproduct")

    return redirect("vendor:manageproduct")

@login_required
def delete_order(request,order_id):
    if request.method == "POST":
        order = Order.objects.get(pk=order_id)
        if order.seller == request.user:
            order.delete()
            return redirect("vendor:manageorder")
    return redirect("vendro:manageorder")

@login_required
def dispatch_order(request,order_id):
    if request.method == "POST":
        order = Order.objects.get(pk=order_id)
        if order.seller == request.user:
            order.order_status = "DP"
            order.save()
            return redirect("vendor:manageorder")

    return redirect("vendor:manageorder")


