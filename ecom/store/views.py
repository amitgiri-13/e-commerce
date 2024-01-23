from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.contrib.auth import login
from django.db.models import Prefetch

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SignUpForm

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
    if request.method == "GET":
        
        product = get_object_or_404(Product, id=product_id)

        # Get or create the user's cart
        cart= Cart.objects.get_or_create(customer=request.user)

        # Check if the product is already in the cart
        cart_item, item_created = CartItems.objects.get_or_create(cart=cart, product=product)

        # If the item is already in the cart, increase the quantity
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('my_carts')  # Redirect to the cart view or wherever you want

