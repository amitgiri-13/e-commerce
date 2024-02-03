from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order,Profile
from django import forms

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


class PasswordResetConfirmForm(forms.Form):
    new_password = forms.CharField(label='new_password', widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(label='confirm_pssword', widget=forms.PasswordInput)
