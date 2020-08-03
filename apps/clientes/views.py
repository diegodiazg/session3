from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from apps.clientes.models import Cliente
from . import forms
from django.urls import reverse, reverse_lazy
from django.contrib import messages
# Create your views here.


class ClientesListView(ListView):
    """carpeta List View.

    Attributes:
        context_object_name (str): Description
        model (TYPE): Description
        template_name (str): Description
    """

    template_name = 'clientes/index.html'
    model = Cliente
    context_object_name = 'clientes'
    paginate_by =  10

    def get_queryset(self):
        """Filter by type and customer.

        Returns:
            TYPE: Description
        """
        queryset = super(ClientesListView, self).get_queryset()
        queryset = Cliente.objects.all()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ClientesListView, self).get_context_data(**kwargs)
        return context


class ClienteNewView(CreateView):
    """Prduct Create View."""

    template_name = 'clientes/new.html'
    model = Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy('super:clientes-list')

    def get_context_data(self, **kwargs):   # noqa
        context = super(ClienteNewView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.save()

        return super(ClienteNewView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Creacion exito"))
        if 'save-and-add' in self.request.POST:
            return reverse('clientes-list')
        else:
            return reverse('clientes-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))


class ClienteUpdateView(UpdateView):
    """."""

    template_name = 'clientes/edit.html'
    model = Cliente
    form_class = forms.ClienteForm
    pk_url_kwarg = 'id'
    context_object_name = 'cliente'

    def get_queryset(self):
        """Filter by type and customer."""
        queryset = super(ClienteUpdateView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):   # noqa
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)       
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #self.object = form.save(commit=False)
        #self.object.save()

        return super(ClienteUpdateView, self).form_valid(form)

    def get_success_url(self):
        """."""
        messages.add_message(
            self.request, messages.SUCCESS,
            _("Updated success."))
        if 'save-and-add' in self.request.POST:
            return reverse('cliente-new')
        else:
            return reverse('cliente-edit', args=[self.object.id, ])

    def form_invalid(self, form):
        """."""
        messages.add_message(
            self.request, messages.ERROR,
            _("Please correct the error below."))
        return self.render_to_response(self.get_context_data(form=form))

