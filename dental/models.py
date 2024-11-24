from django.db import models
from usuarios.models import Dental

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    validade = models.DateField()
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    #imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    dental = models.ForeignKey(Dental, on_delete=models.CASCADE)  # Relacionamento com o Dental
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome