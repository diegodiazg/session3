# from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$',
        views.HomeListView.as_view(), name='home-list'),
  	url(r'^clientes-lista/$', views.lista_clientes, name='lista-clientes'),
  	url(r'^clientes-crear/$', views.nuevo_cliente, name='crear-clientes'),
  	url(r'^(?P<cliente_id>[\w\- ]+)/$',
  	    views.editar_cliente, name='editar-cliente'),
  	url(r'^(?P<cliente_id>[\w\- ]+)/borrar/$',
  	    views.borrar_cliente, name='borrar-cliente')      	
]	
