# from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$',
        views.HomeListView.as_view(), name='home-list'),
  	url(r'^clientes-lista/$', views.lista_clientes, name='lista-clientes')

]	
