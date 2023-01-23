from django.db import models

# Create your models here.
from shop.models import Product
from ecobot.models import  User_Info

class Order(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    returnable = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,
                                related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity