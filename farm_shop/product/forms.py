from django import forms

from product.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_name', 'user_email',
                  'user_phone', 'user_message')


