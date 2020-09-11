# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from apps.clientes.models import Cliente

class HomeListView(TemplateView):

    template_name = 'home/index.html'

def lista_clientes(request):
	clientes = Cliente.objects.all()
	dic = { 'clientes': clientes }
	
	return render(request, 'home/lista-clientes.html', dic)