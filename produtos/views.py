from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from produtos.models import Produto
from produtos.forms import CadastroForm

# Create your views here.

class ProdutoList(ListView):
    model = Produto
    queryset = Produto.objects.all()

class ProdutoCreate(CreateView):
    model = Produto
    form_class = CadastroForm
    #fields = '__all__'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = CadastroForm
    #fields = '__all__'
    success_url = reverse_lazy('produto_list')

class ProdutoDetail(DetailView):
    queryset = Produto.objects.all()

class ProdutoDelete(DeleteView):
    queryset = Produto.objects.all()
    success_url = reverse_lazy('produto_list')


## login

def home(request):
    return render(request, 'produtos/home.html', context={})

def caduser(request):
    context = { 'cuser': '', 'cemail': '' }
    return render(request, 'produtos/caduser.html', context)

def store(request):
    context = {}
    if request.method == "POST":
        if request.POST['password'] != request.POST['password-conf']:
            context['erro'] = 'true'
            context['cuser'] = request.POST['user']
            context['cemail'] = request.POST['email']
            context['erroSenha'] = 'A confirmação de senha deve ser igual à senha escolhida!'
            context['class'] = 'alert-danger'   
        else:
            user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
            user.save()
            context['success'] = 'Cadastro realizado com sucesso!'
            context['class'] = 'alert-success' 
    return render(request, 'produtos/caduser.html', context)

def painel(request):
    return render(request, 'produtos/painel.html', context={})

def dologin(request):
    return redirect(request, 'produtos/painel.html')




