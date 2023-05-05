from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Usuário')
    date_ordered = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Data do Pedido')
    transaction_id = models.CharField(max_length=100, null=True,
                                      verbose_name='ID da Transação')
    quantity = models.PositiveIntegerField()
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('C', 'Criado'),
            ('A', 'Aprovado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N° {self.pk} - ID: {self.transaction_id}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    varitation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.order}'

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
