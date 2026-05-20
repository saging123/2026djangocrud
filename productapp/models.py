from django.db import models

class Product(models.Model):
    rowid = models.BigAutoField(primary_key=True)
    productid = models.CharField(
        max_length=30,
        unique=True,
        db_index=True,
        verbose_name="Product ID"
    )
    name = models.CharField(
        max_length=255
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        