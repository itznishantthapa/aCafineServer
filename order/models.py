from django.db import models
from authentication.models import CustomUser
from dish.models import Dish



# Create your models here.
# Order Model
class Order(models.Model):
    ORDER_MODE = [
        ('EAT', 'Eat at Canteen'),
        ('PACK', 'Packed Takeaway')
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=True)
    is_ready = models.BooleanField(default=False)
    eat_mode = models.CharField(max_length=4, choices=ORDER_MODE, default='EAT')
    esewa_transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"




#Here this tables allows user to order the different dishes
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)