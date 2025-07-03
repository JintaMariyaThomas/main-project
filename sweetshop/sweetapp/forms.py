from django import forms
from .models import Order
from django.contrib.auth.forms import AuthenticationForm


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'address']
        labels = {
            'customer_name': 'Your Name',
            'customer_email': 'Email',
            'address': 'Shipping Address',
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-username'  # random value, blocks browser autofill
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password'  # random value
        })
    )




