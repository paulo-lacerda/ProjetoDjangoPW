from django.contrib import admin
from Sistema.models import Cliente, Produto, Usuario, Distribuidor

admin.site.register(Usuario)
admin.site.register(Distribuidor)
admin.site.register(Produto)
admin.site.register(Cliente)