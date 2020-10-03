# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect, redirect

from apps.clientes.models import Cliente
from apps.clientes import forms
from django.urls import reverse

class HomeListView(TemplateView):

    template_name = 'home/index.html'

def lista_clientes(request):
	clientes = Cliente.objects.all()
	dic = { 'clientes': clientes, 'autor': 'Diego' }
	return render(request, 'home/lista-clientes.html', dic)

def nuevo_cliente(request):
  context ={}
  form = forms.ClienteForm(request.POST or None)

  if form.is_valid():
    # SI EL FORMULARIO ES VALIDO SE GUARDAR EL DATO
    instance = form.save()
    # SE REDIRIGE AL FORMULARIO DE EDITAR    
    return redirect('editar-cliente', cliente_id=instance.id)
    


  context['form']= form
  return render(request, "home/crear-cliente.html", context)


def editar_cliente(request, cliente_id):

  try:
    cliente = Cliente.objects.get(pk=cliente_id)
  except Cliente.DoesNotExist:
    return render(request, 'home/404.html')
  
  form = forms.ClienteForm(request.POST or None, instance=cliente)

  if form.is_valid():
    form.save()

  context = {'form': form}
  return render(request, 'home/editar-cliente.html', context)

def borrar_cliente(request, cliente_id):
  
  try:
    cliente = Cliente.objects.get(pk=cliente_id)
  except Cliente.DoesNotExist:
    return render(request, 'home/404.html')

  if request.method == 'POST':
    try:      
      cliente.delete()       
    except Exception as e:
      print(e.__class__.__name__)
      return e

    return HttpResponseRedirect("/clientes-lista/") 
  
  context = {'cliente': cliente}
  return render(request, 'home/borrar-cliente.html', context)



