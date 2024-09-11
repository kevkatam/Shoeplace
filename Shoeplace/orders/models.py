from django.db import models
from products.models import Product


# Create your models here.
class Order(models.Model):
    """ model to represent a single product in the order """
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def get_total_cost(self):
        """ 
        gets the total amount that should be paid
        sum of the items in the order
        """
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """ model to represent a single item in the order """
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def get_cost(self):
        """gets total cost of the item """
        return self.price * self.quantity
