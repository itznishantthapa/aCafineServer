from django.db import models

# Canteen Menu
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name