import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
    ]

    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'), 
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)
    available_sizes = models.CharField(max_length=200, null=True, help_text="Sizes separated by commas")
    product_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_sizes_list(self):
        """Return list of available sizes"""
        if self.available_sizes:
            return [size.strip() for size in self.available_sizes.split(',')]
        return []
    
    def set_sizes_list(self, sizes_list):
        """Set available sizes from list"""
        self.available_sizes = ', '.join(sizes_list)
    
    @property
    def is_popular(self):
        return self.product_views > 30
    
    def increment_views(self):
        self.product_views += 1
        self.save()