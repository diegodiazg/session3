from django.forms import ModelForm, Textarea
from apps.clientes.models import Cliente

from django import forms


class ClienteForm(ModelForm):

    first_name = forms.CharField(label='First name',)
    last_name = forms.CharField(label= 'Purchase price',initial=0, )        

    class Meta:
        model = Cliente
        fields = (
        	'first_name',
        	'last_name',
        	'address',
        	'phone', 
        	'phone',
        	'email',
            'status'
       		)
        