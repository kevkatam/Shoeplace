from django.db import models
from products.models import Product


# Create your models here.
class Cart(models.Model):
    """ class representing Cart model """
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        """ gets total price of items in a cart """
        return sum(item.get_total_price() for item in self.items.all())

    def __str__(self):
        """ string representation of the Cart model """
        return f"Cart created on {self.created_at}"

class CartItem(models.Model):
    """ class representing CartItem model """
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        """ gets total price of multiple items in a cart """
        return self.product.price * self.quantity

    def __str__(self):
        """ string representation of cartitem model """
        return f"{self.quantity} of {self.product.name} in Cart"
