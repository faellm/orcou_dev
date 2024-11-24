from django.shortcuts import render
from django.shortcuts import get_object_or_404
from usuarios.models import Dentista, Dental

# Create your views here.
def perfil_dentista(request, user_id):
    # Busca o usuário dentista pelo ID
    dentista = Dentista.objects.filter(pk=user_id)
    
    # Agora você pode usar o objeto 'dentista' na lógica da sua view
    return render(request, 'perfil_dentista.html', {'dentista': dentista})
