from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('login/', views.login, name='login'),
    path('cadastro_dental/', views.cadastro_dental, name='cadastro_dental'),
    path('cadastro_dentista/', views.cadastro_dentista, name='cadastro_dentista'),
    
] 