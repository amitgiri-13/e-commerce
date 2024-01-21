from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth import login


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
    template_name = "store/home.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.prefetch_related("product_set")
    

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
