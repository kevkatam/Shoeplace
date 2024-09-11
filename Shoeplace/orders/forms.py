from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """ form for create order view """
    class Meta:
        model = Order
        fields = ["full_name", "email", "address"]
