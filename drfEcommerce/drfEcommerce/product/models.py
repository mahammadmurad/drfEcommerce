from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=235, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

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
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category", on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.name


# Create your models here.
