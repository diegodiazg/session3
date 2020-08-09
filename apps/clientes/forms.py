from django.forms import ModelForm, Textarea
from apps.clientes.models import Cliente

from django import forms


class ClienteForm(ModelForm):

    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(label= 'Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}) )
    address = forms.CharField(label= 'Dirección', widget=forms.Textarea( attrs={'class': 'form-control', 'rows':'5','cols':'12' }) )
    phone = forms.CharField(label= 'Teléfono', widget=forms.NumberInput(attrs={'class': 'form-control'}) )
    email = forms.CharField(required=False, label= 'Email', widget=forms.TextInput(attrs={'class': 'form-control'}) )
    status = forms.BooleanField(required=False, initial=True, label= 'Estado', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}) )

    class Meta:
        model = Cliente
        fields = (
        	'first_name',
        	'last_name',
        	'address',
        	'phone',
        	'email',
            'status'
       		)
        