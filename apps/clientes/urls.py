
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.ClientesListView.as_view(), name='clientes-list'),
    url(r'^new/$',
        views.ClientesNewView.as_view(), name='clientes-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.ClientesUpdateView.as_view(), name='clientes-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.ClientesDeleteView.as_view(), name="clientes-delete"),

    #CRUD BASICO
	url(r'^crud-r/$', views.crud_r, name='crud-r'),
	url(r'^crud-c/$', views.crud_c, name='crud-c'),
	url(r'^crud-u/(?P<cliente_id>[\w\- ]+)/edit/$', views.crud_u, name='crud-u'),
    url(r'^crud-d/(?P<cliente_id>[\w\- ]+)/delete/$', views.crud_d, name='crud-d')

]


