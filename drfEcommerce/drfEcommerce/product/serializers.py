from rest_framework import serializers
from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="name")
    class Meta:
        model = Category
        exclude = ('id',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["category", "slug"]


class ProductLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductLine
        exclude = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        exclude = ("id",)
