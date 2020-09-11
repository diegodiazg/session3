# from django.urls import path
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$',
        views.HomeListView.as_view(), name='home-list'),
    
    path('custom-clientes', views.lista_clientes, name='lista-clientes'),
    path('<uuid:cliente_id>/', views.detalle_clientes, name='detalle-clientes'),
     

]
