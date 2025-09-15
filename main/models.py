import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    product_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    @property
    def is_popular(self):
        return self.product_views > 30
    
    def increment_views(self):
        self.product_views += 1
        self.save()