from django.db import models

# Canteen Menu
class Dish(models.Model):
    DISH_TYPE = [
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non-Vegetarian'),
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('drinks', 'Drinks')
    ]

    title = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='dishes/', blank=True)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=10, choices=DISH_TYPE)
    is_veg=models.BooleanField(default=False)

    def __str__(self):
        return self.title
        