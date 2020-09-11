# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from django.http import Http404
from django.shortcuts import render

from apps.clientes.models import Cliente


class HomeListView(TemplateView):

    template_name = 'home/index.html'
    
    
def detalle_clientes(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:        
        return render(request, 'home/404.html')

    context = {'cliente': cliente}
    return render(request, 'home/detalle_cliente.html', context)

def lista_clientes(request):	
	
	try:
		lista_clientes = Cliente.objects.order_by('-created_at')[:5]
	except Exception as e:
		raise Http404(str(e))

	dic = {'clientes': lista_clientes }
	return render(request, 'home/lista_clientes.html', dic )