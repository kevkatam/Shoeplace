from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    """ class representing Category model"""
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """ string representation of the model """
        return self.name


class Product(models.Model):
    """ class representing Product model """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length =250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created =  models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        """ string representation of Product model """
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'id':self.id, 'slug':self.slug})
