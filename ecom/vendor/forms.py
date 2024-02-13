from django.forms import ModelForm
from store.models import Product

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product 
        fields = [
            "category",
            "product",
            "description",
            "price",
            "image",
        ]