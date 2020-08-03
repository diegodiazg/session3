
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.ClientesListView.as_view(), name='clientes-list'),

]


