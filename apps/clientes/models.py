from django.db import models
import uuid

# Create your models here.

class Cliente(models.Model):	

	    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	    first_name = models.CharField( null=False,max_length=255,
	        blank=False, verbose_name='Firts name')
	    last_name = models.CharField(max_length=255,
	       null=False, blank=False, verbose_name='Last name')
	    address = models.CharField(max_length=400,
	       null=False, blank=False, verbose_name='Address')
	    phone = models.CharField(max_length=20,
	        null=False, blank=False, verbose_name='Phone')
	    email = models.EmailField(
	        null=False, blank=False, verbose_name='Email')

	    status = models.BooleanField(
	        default=True,  verbose_name='Status')
	    created_at = models.DateTimeField(auto_now_add=True)
	    updated_at = models.DateTimeField(auto_now=True)

	    class Meta:  # noqa
	        verbose_name = 'Cliente'
	        verbose_name_plural = 'Clientes'
	        default_related_name = 'cliente'
	        db_table = 'clientes'
	        #ordering = ['-created_at']

	    def __unicode__(self):
	        u"""Customer."""
	        # return u'%s' % self.full_name
	        return str(self.full_name)

	    def __str__(self):
	            return '%s' % (self.full_name)

	    @property
	    def full_name(self):
	        """Nombre completo del cliente.

	        :attribute: full_name
	        :type: String
	        :return: self.get_full_name()
	        """
	        return self.get_full_name()

	    def get_full_name(self):
	        u"""Devuelve el nombre completo del cliente.

	        Devuelve una unión de el nombre y el apellido del cliente.

	        :return: u'%s %s' % (self.first_name, self.last_name)
	        """
	        return u'%s %s' % (self.first_name, self.last_name)
	
		