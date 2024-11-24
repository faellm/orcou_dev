from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('perfil_dental/<int:user_id>/', views.perfil_dental, name='perfil_dental'),
    path('criar_produto/<int:user_id>/', views.criar_produto, name='criar_produto'),
]   