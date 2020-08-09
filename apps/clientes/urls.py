
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

]


