from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Dental
from dental.models import Produto
from django.contrib import messages
import datetime

# Create your views here.
def perfil_dental(request, user_id):
    dental = get_object_or_404(Dental, id=user_id)
    produto = Produto.objects.filter(dental=user_id)
    context = {'dental': dental,
                'produto':produto}
    return render(request, 'perfil_dental.html', context)

def criar_produto(request, user_id):
    if request.method == 'POST':
        # Recupera os valores do POST
        nome = request.POST.get('nameprod')
        validade = request.POST.get('validade')
        estoque = request.POST.get('estoque')
        preco = request.POST.get('preco')
        descricao = request.POST.get('desc')
        imagem = request.FILES.get('imagem_produto')  # Obtém o arquivo enviado (imagem do produto)
        
        # Valida se todos os campos necessários estão preenchidos
        if nome and validade and estoque and preco and descricao:
            dental_instance = get_object_or_404(Dental, id=user_id)
            # Cria o objeto Produto com os dados do formulário
            produto = Produto(
                nome=nome,
                validade= datetime.datetime.strptime(validade, '%d/%m/%Y').date(),
                estoque=estoque,
                preco=preco,
                descricao=descricao,
                dental=dental_instance
            )
            produto.save()  # Salva o produto no banco de dados
            
            produto = Produto.objects.filter(dental=user_id)
            
            context = {
                'message': 'sucesso',
                'produto': produto,
                'dental': dental_instance
            }
            return render(request, 'perfil_dental.html', context)
        else:
            # Caso algum campo obrigatório esteja faltando
            context = {
                    'message': 'erro',
                }
            return render(request, 'perfil_dental.html', context)
   