from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField( upload_to="shop", null = True, blank = True )
    price = models.FloatField()
    stock = models.BooleanField(default = True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name