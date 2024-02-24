from django.db import models
from mptt.models import TreeForeignKey, MPTTModel

from .fields import OrderField

class IsActiveQueryset(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)


class Category(MPTTModel):
    name = models.CharField(max_length=235, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    objects = IsActiveQueryset.as_manager()

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=235,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category", on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    objects = IsActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField(max_length=10)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product", blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    objects = IsActiveQueryset.as_manager()
    
    def clean(self):
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order
    def __str__(self):
        return str(self.sku)


# Create your models here.
