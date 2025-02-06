from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    ENTREGA = 'entrega'
    RETIRADA = 'retirada'
    TIPO_ENTREGA_CHOICES = [
        (ENTREGA, 'Entrega'),
        (RETIRADA, 'Retirada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    tipo_entrega = models.CharField(max_length=10, choices=TIPO_ENTREGA_CHOICES)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_total(self):
        self.total = sum(produto.preco for produto in self.produtos.all())
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nome}"
