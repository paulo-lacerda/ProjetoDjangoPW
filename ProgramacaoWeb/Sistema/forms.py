from django.forms.models import ModelForm
from Sistema.models import Cliente, Produto, Usuario

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        exclude=['id']
        
class ProdutoForm(ModelForm):
    class Meta:
        model=Produto
        exclude=['id']
        
class UsuarioForm(ModelForm):
    class Meta:
        model=Usuario
        exclude=['id']
        
