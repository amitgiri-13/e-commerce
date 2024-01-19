from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth import login

# Create your views here.
from .models import *
from .forms import SignUpForm

class IndexView(generic.TemplateView):
    template_name = "store/home.html"

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "sotre/detail.html"
    

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

