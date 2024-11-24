from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .models import Dentista, Dental
from .models import ClienteManager
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('usr')
        senha = request.POST.get('pass')
        
        # Primeiro tenta encontrar o usuário no modelo Dental
        try:
            user = Dental.objects.get(email=email)
        except Dental.DoesNotExist:
            user = None

        # Se não encontrar no Dental, tenta buscar no modelo Dentista
        if not user:
            try:
                user = Dentista.objects.get(email=email)
            except Dentista.DoesNotExist:
                user = None
        
        # Se não encontrar em ambos, tenta buscar no modelo User (superusuário)
        if not user:
            user = User.objects.filter(email=email).first()  # Usando .filter() para evitar o DoesNotExist

        if user:
            # Autentica o usuário com o método padrão do Django
            if user.check_password(senha):  # Verifica a senha
                # Verifica o tipo de usuário, se aplicável
                if hasattr(user, 'tipo'):
                    if user.tipo == 'dentista':
                        auth_login(request, user)
                        return redirect('perfil_dentista', user_id=user.id)
                    elif user.tipo == 'dental':
                        auth_login(request, user)
                        return redirect('perfil_dental', user_id=user.id)
                else:
                    # Login para superusuário
                    auth_login(request, user)
                    return redirect('painel_admin')
            else:
                return HttpResponse('Credenciais inválidas')
        else:
            return HttpResponse('Usuário não encontrado')

    return render(request, 'login-dashboard.html')

def cadastro_dentista(request):
    
    if request.method == 'POST':
        primeiro_nome = request.POST.get('primeiro_nome')
        segundo_nome = request.POST.get('segundo_nome')
        #nome_completo = request.POST.get('segundo_nome')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        contato = request.POST.get('contato')
        email = request.POST.get('email')
        sexo = request.POST.get('sexo')
        senha = request.POST.get('pass')
        data_nascimento = request.POST.get('data_nascimento')
        tipo = 'dentista'
        
        # Verifica se o email já está em uso
        if Dentista.objects.filter(email=email).exists():
            return HttpResponse('Email já cadastrado como dentista.')

        # Cria o dentista
        # Cria o dentista
        dentista = Dentista.objects.create_user(
            primeiro_nome=primeiro_nome,
            segundo_nome=segundo_nome,
            sexo=sexo,
            data_nascimento=data_nascimento,
            email=email,
            password=senha,
            contato=contato,
            cpf=cpf,
            cep=cep,
            tipo='dentista'
        )
        auth_login(request, dentista)
        return redirect('perfil_dentista', user_id=dentista.id)

    return render(request, 'cadastro_dentista.html')
    
def cadastro_dental(request):
    
    if request.method == 'POST':
        nome_empresa = request.POST.get('nome_empresa')
        email = request.POST.get('email')
        #nome_completo = request.POST.get('segundo_nome')
        cnpj = request.POST.get('cnpj')
        contato = request.POST.get('contato')
        end = request.POST.get('end')
        comp = request.POST.get('comp')
        num = request.POST.get('num')
        senha = request.POST.get('pass')
        data_cadastro = request.POST.get('data_cadastro')
        
        # Verifica se o email já está em uso
        if Dental.objects.filter(email=email).exists():
            return HttpResponse('Email já cadastrado.')

        dental = Dental.objects.create_user(
            nome_empresa=nome_empresa,
            email=email,
            cnpj=cnpj,
            contato=contato,
            end=end,
            password=senha,
            comp=comp,
            num=num,
            data_cadastro=data_cadastro,
            tipo='dental'
        )
        auth_login(request, dental)
        return redirect('perfil_dental', user_id=dental.id)

    return render(request, 'cadastro_dental.html')