from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('perfil_dentista/<int:user_id>/', views.perfil_dentista, name='perfil_dentista'),
] 
