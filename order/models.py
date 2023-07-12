from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model() 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['id']

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.order_detail_set.aggregate(
            total = Sum(F("price")*F("amount"), output_field = FloatField())
        )["total"]

class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    amount = models.IntegerField(default = 1)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'order_detail'
        verbose_name = 'order detail'
        verbose_name_plural = 'order details'
        ordering = ['id']

    def __str__(self):
        return f'{self.amount} unidades de {self.product.name}'
    
