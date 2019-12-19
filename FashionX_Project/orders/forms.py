from django import forms 
from .models import Order,OrderReciepts


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        
class OrderRecieptForm(forms.ModelForm):
    class Meta:
        model=OrderReciepts
        fields='__all__'