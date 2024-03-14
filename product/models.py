from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_info = models.CharField(max_length=500)
    quantity = models.IntegerField()
    price = models.DecimalField(max_length=19, decimal_places=2)
    product_type = models.CharField(max_length=11)
    product_image = models.ImageField()

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.id)
