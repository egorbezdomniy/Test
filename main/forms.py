from django import forms
from . import models


class LiquidForm(forms.ModelForm):
    class Meta:
        model = models.Liquid
        fields = ['name', 'price', 'brand', 'amount', 'margin', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'margin': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
        }


class PodForm(forms.ModelForm):
    class Meta:
        model = models.Pod
        fields = ['name', 'price', 'brand', 'amount', 'margin', 'description', 'battery']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'margin': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),

        }
class SingleForm(forms.ModelForm):
    class Meta:
        model = models.Single
        fields = ['name', 'price', 'brand', 'amount', 'margin', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'margin': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            
        }

class EvaporatorForm(forms.ModelForm):
    class Meta:
        model = models.Evaporator
        fields = ['name', 'price', 'brand', 'amount', 'margin', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'margin': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = models.Sale
        fields = ['sold_for', 'date', 'amount_of_sold', 'object_id', 'content_type',]

        widgets = {
            'amount_of_sold': forms.DateInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sold_for': forms.TextInput(attrs={'class': 'form-control'}),
            'object_id': forms.TextInput(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-control'}),
        }
    
    
