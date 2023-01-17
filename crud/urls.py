"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', views.ProdutoList.as_view(), name='produto_list'),
    path('create/', views.ProdutoCreate.as_view(), name='produto_create'),
    path('update/<int:pk>/', views.ProdutoUpdate.as_view(), name='produto_update'),
    path('detail/<int:pk>/', views.ProdutoDetail.as_view(), name='produto_detail'),
    path('delete/<int:pk>/', views.ProdutoDelete.as_view(), name='produto_delete'),
    path('home/', views.home, name='home'),
    path('caduser/', views.caduser, name='caduser'),
    path('store/', views.store, name='store'),
    path('painel/', views.painel, name='painel'),
    path('dologin/', views.dologin, name='dologin')
]
