"""ProgramacaoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, handler404
from django.contrib import admin

urlpatterns = [
    
        ############################################ CLIENTES ######################3

    
    url(r'^cliente/$','Sistema.views.cliente',name='sistema_cliente'),
    url(r'^cliente_novo/$','Sistema.views.create',name='cliente_create'),
    url(r'^cliente/(?P<pk>\d+)/$','Sistema.views.cliente_update',name='cliente_update'),
    url(r'^cliente_delete/(?P<pk>\d+)/$','Sistema.views.delete',name='cliente_delete'),
    
        ############################################ PRODUTOS ######################3

    
    url(r'^produto/$','Sistema.views.produto',name='sistema_produto'),
    url(r'^produto_novo/$','Sistema.views.createproduto',name='produto_create'),
    url(r'^produto/(?P<pk>\d+)/$','Sistema.views.produto_update',name='produto_update'),
    url(r'^produto_delete/(?P<pk>\d+)/$','Sistema.views.deleteproduto',name='produto_delete'),
    
        ############################################ USUARIOS ######################3

    
    url(r'^usuario/$','Sistema.views.usuario',name='sistema_usuario'),
    url(r'^usuario_novo/$','Sistema.views.createusuario',name='usuario_create'),
    url(r'^usuario/(?P<pk>\d+)/$','Sistema.views.usuario_update',name='usuario_update'),
    url(r'^usuario_delete/(?P<pk>\d+)/$','Sistema.views.deleteusuario',name='usuario_delete'),
    
    
    ############################################ LOGIN ######################3
    

    url(r'^$' , 'django.contrib.auth.views.login', {'template_name':'LOGIN.html'}, name= 'login'),
    url(r'^sair/$' , 'django.contrib.auth.views.logout_then_login', name= 'logout'),
    
    
    url(r'^home/$','Sistema.views.home', name='sistema_home' ),
    url(r'^admin/', include(admin.site.urls)),
    

    
]


        