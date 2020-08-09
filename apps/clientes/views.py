from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.clientes.models import Cliente
from . import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Value
from django.db.models.functions import Concat

class ClientesListView(ListView):    

    template_name = 'clientes/index.html'
    model = Cliente
    context_object_name = 'clientes'
    paginate_by =  4

    def get_queryset(self):        
        queryset = super(ClientesListView, self).get_queryset()        

        queryset = Cliente.objects.all()        
        if 'name' in self.request.GET:
            name = self.request.GET['name']
            queryset = queryset.annotate(search_name=Concat('first_name', Value(' '), 'last_name'))
            queryset = queryset.filter(search_name__icontains=name)

        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ClientesListView, self).get_context_data(**kwargs)

        if 'name' in self.request.GET:
            name = self.request.GET['name']            
            context['name'] = name

        return context


class ClientesNewView(CreateView):    

    template_name = 'clientes/new.html'
    model = Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy('super:clientes-list')

    def get_context_data(self, **kwargs):   # noqa
        context = super(ClientesNewView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):        
        self.object = form.save(commit=False)
        self.object.save()

        return super(ClientesNewView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            "Creación exitosa")
        if 'save-and-add' in self.request.POST:
            return reverse('clientes-list')
        else:
            return reverse('clientes-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            "Por favor corrige los errores de abajo.")
        return self.render_to_response(self.get_context_data(form=form))


class ClientesUpdateView(UpdateView):
    """."""

    template_name = 'clientes/edit.html'
    model = Cliente
    form_class = forms.ClienteForm
    pk_url_kwarg = 'id'
    context_object_name = 'cliente'

    def get_queryset(self):        
        queryset = super(ClientesUpdateView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ClientesUpdateView, self).get_context_data(**kwargs)       
        return context

    def form_valid(self, form):
        return super(ClientesUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            "Actualización exitosa.")
        if 'save-and-add' in self.request.POST:
            return reverse('clientes-new')
        else:
            return reverse('clientes-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            "Por favor corrige los errores de abajo.")
        return self.render_to_response(self.get_context_data(form=form))


class ClientesDeleteView(DeleteView):
    """."""

    template_name = 'clientes/delete.html'
    model = Cliente
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        """Judge Delete."""
        context = super(ClientesDeleteView, self).get_context_data(**kwargs)

        cliente = get_object_or_404(Cliente, id = self.object.id)             
        context['cliente'] = cliente
      
        return context

    def get_queryset(self):        
        queryset = super(ClientesDeleteView, self).get_queryset()
        return queryset

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            "El objeto se ha borrado exitosamente")
        return reverse('clientes-list')