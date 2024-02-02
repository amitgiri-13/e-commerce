from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order,Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model  = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            "receiver_name",
            "quantity",
            "order_address",
            "contact_number",
        ]

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "address"
        ]
        