from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Gerenciador de Usuários
class ClienteManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O endereço de email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Usa o método para criptografar a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Dentista(AbstractBaseUser):
    primeiro_nome = models.CharField(max_length=200, null=True)
    segundo_nome = models.CharField(max_length=200, null=True)
    nome_completo = models.CharField(max_length=200, null=True)
    cpf = models.CharField(max_length=14, unique=True, null=True)
    cep = models.CharField(max_length=14, null=True)
    contato = models.CharField(max_length=14, null=True)
    email = models.EmailField(max_length=200, unique=True, null=False)
    sexo = models.CharField(max_length=15, null=True)
    tipo = models.CharField(max_length=15, null=True)  # 'dentista'
    data_nascimento = models.DateField(help_text="Informe a data no formato dd/mm/aaaa", null=True)
    data_registro = models.DateTimeField(auto_now_add=True, null=True)

    # Campos de autenticação
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Definição de campos de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClienteManager()

    class Meta:
        ordering = ['id']
        default_related_name = 'dentistas'

    def __str__(self):
        return self.email


class Dental(AbstractBaseUser):  # Herda de AbstractBaseUser para suportar login
    nome_empresa = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=False)
    cnpj = models.CharField(max_length=14, unique=True, null=True)
    contato = models.CharField(max_length=14, null=True)
    end = models.CharField(max_length=45, null=True)
    tipo = models.CharField(max_length=15, null=True)  # 'dental'
    comp = models.CharField(max_length=15, null=True)
    num = models.CharField(max_length=5, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    data_registro = models.DateField(null=True)

    # Campos de autenticação
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Definição de campos de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClienteManager()

    class Meta:
        ordering = ['id']
        default_related_name = 'dentals'

    def __str__(self):
        return self.email