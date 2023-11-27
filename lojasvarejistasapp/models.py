from django.db import models


# O arquivo models.py no Django é usado para definir a estrutura dos dados 
# que serão armazenados no banco de dados do aplicativo. Ele contém os campos 
# e comportamentos desses dados. Cada modelo vai equivaler à uma tabela 
# no banco de dados.

# Modelo Loja
class Loja(models.Model):
    id_loja = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=30)
    horario_atendimento = models.CharField(max_length=40)


# Modelo Produto
class Produto(models.Model):
    id_produto = models.CharField(max_length=10, primary_key=True)
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    lote = models.CharField(max_length=20)

# Modelo VendeProduto
class VendeProduto(models.Model):
    preco = models.FloatField()
    loja = models.CharField(max_length=25)
    produto = models.CharField(max_length=25)

