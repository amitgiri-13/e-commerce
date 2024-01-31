from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.contrib.auth import login
from django.db.models import Prefetch

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SignUpForm

class ProfileView(generic.DetailView):
    model = Profile
    template_name = "store/profile.html"
    context_object_name = "profile"

    def get_object(self):
        return self.request.user.profile
    

class IndexView(generic.ListView):
    model = Category
    template_name = "store/home.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.prefetch_related("product_set")
    
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "store/detail.html"
    context_object_name = "product"
    
class NewArrivalView(generic.ListView):
    model = Category
    template_name = "store/newarrivals.html"
    context_object_name = "category_list"

    def get_queryset(self):
        queryset = Category.objects.prefetch_related(Prefetch("product_set",queryset=Product.objects.all()[:3],to_attr="latest_product"))
        return queryset

class MyCartView(generic.ListView):
    model = CartItems
    template_name = "store/mycart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return CartItems.objects.filter(cart__customer=self.request.user)
    
class OrderView(generic.ListView):
    model = Order
    template_name = "store/order.html"
    context_object_name = "order_list"

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)
    

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
           
            user = form.save()  
            login(request,user)

            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'store/signup.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(customer=request.user)
        cart_item, item_created = CartItems.objects.get_or_create(cart=cart, products=product)
        if not item_created:
            cart_item.save()

    return redirect('my_carts')

@login_required
def remove_from_cart(request,item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItems,products_id=item_id)
        cart_item.delete()

    return redirect("my_carts")

def search_items(request):
    query = request.POST.get('search_by')
    if query:
        objects = Product.objects.filter(
                models.Q(product__icontains=query) |
                models.Q(description__icontains=query)
            )
        return render(request,'store/search_results.html',{'product_list':objects})
    
    return redirect("home")

