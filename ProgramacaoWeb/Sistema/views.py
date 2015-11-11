from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from Sistema.models import Cliente, Produto, Usuario
from Sistema.forms import ClienteForm, ProdutoForm, UsuarioForm
from django.template.context_processors import request


def home(request):
    #data={}
    #data['usuarioLogado'] = Usuario.objects.filter(pk=1).get()
    return render(request, 'HOME.html')

def cliente(request):
    data={}
    data['lista_clientes'] = Cliente.objects.all()
    return render(request, 'CLIENTE.html', data)

def cliente_update(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('sistema_cliente')
    return render(request,'CLIENTE_DETALHE.html',{'object':cliente,'form':form})
        
        
    return render(request, 'CLIENTE_DETALHE.html', {'object':cliente})

def create(request):
    form = ClienteForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('sistema_cliente')
    else:
        return render(request,'CLIENTE_NOVO.html',{'form':form})
    
def delete(request,pk):
    cliente = Cliente.objects.get(pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('sistema_cliente')
    return render(request, 'CLIENTE_DELETE_CONFIRM.html',{'object':cliente})

######################## PRODUTO ###############################

def produto(request):
    data={}
    data['lista_produtos'] = Produto.objects.all()
    return render(request, 'PRODUTO.html', data)

def produto_update(request, pk):
    produto = Produto.objects.get(pk=pk)
    
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('sistema_produto')
    return render(request,'PRODUTO_DETALHE.html',{'object':produto,'form':form})
        
        
    return render(request, 'PRODUTO_DETALHE.html', {'object':produto})

def createproduto(request):
    form = ProdutoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('sistema_produto')
    else:
        return render(request,'PRODUTO_NOVO.html',{'form':form})
    
def deleteproduto(request,pk):
    produto = Produto.objects.get(pk=pk)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('sistema_produto')
    return render(request, 'PRODUTO_DELETE_CONFIRM.html',{'object':produto})
    
    
    
    ############################## USUARUI ################################
    
    
def usuario(request):
    data={}
    data['lista_usuarios'] = Usuario.objects.all()
    return render(request, 'USUARIO.html', data)

def usuario_update(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('sistema_usuario')
    return render(request,'USUARIO_DETALHE.html',{'object':usuario,'form':form})
        
        
    return render(request, 'USUARIO_DETALHE.html', {'object':usuario})

def createusuario(request):
    form = UsuarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('sistema_usuario')
    else:
        return render(request,'USUARIO_NOVO.html',{'form':form})
    
def deleteusuario(request,pk):
    usuario = Usuario.objects.get(pk=pk)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('sistema_usuario')
    return render(request, 'USUARIO_DELETE_CONFIRM.html',{'object':usuario})
    



