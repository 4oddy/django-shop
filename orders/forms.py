from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Иван'}))
    telefon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': '+79617775818'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'you@mail.ru'}))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Екатеринбург, ул. Мира, дом 6'}))

    class Meta:
        model = Order
        fields = ('first_name', 'telefon', 'email', 'location')
