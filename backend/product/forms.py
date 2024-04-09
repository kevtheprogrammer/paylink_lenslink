from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
 

from .models import *
 

 
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'quantity',
            ]


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
			# 'orderitems',
			'email',
			'address',
			'city',
			'state',
			'zip_code',
			# 'shipping_fee',
			)
        # widgets = {
        #     'orderitems': forms.CheckboxSelectMultiple,
        # }