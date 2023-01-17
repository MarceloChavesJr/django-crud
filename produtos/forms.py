from django import forms

from produtos.models import Produto

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'preco', 'fabricante', 'quantidade')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fabricante'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
        }
         