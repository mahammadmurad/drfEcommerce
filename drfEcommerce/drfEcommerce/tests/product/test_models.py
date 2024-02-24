from drfEcommerce.product.models import *

class TestCategoryModel:
    def test_str_method_(self, category_factory):
        x = category_factory.get_category()
        assert x.__str__() == 'test_category'


class TestBrandModel:
    pass


class TestProductModel:
    pass


class TestProductModel:
    def test_str_method(self, product_factory):
        obj = product_factory(name="test_product")
        assert obj.__str__() == "test_product"

    def test_fk_product_type_on_delete_protect(
        self, product_type_factory, product_factory
    ):
        obj1 = product_type_factory()
        product_factory(product_type=obj1)
        with pytest.raises(IntegrityError):
            obj1.delete()

    def test_name_max_length(self, product_factory):
        name = "x" * 236
        obj = product_factory(name=name)
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_slug_max_length(self, product_factory):
        slug = "x" * 256
        obj = product_factory(slug=slug)
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_pid_length(self, product_factory):
        pid = "x" * 11
        obj = product_factory(pid=pid)
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_is_digital_false_default(self, product_factory):
        obj = product_factory(is_digital=False)
        assert obj.is_digital is False

    def test_fk_category_on_delete_protect(self, category_factory, product_factory):
        obj1 = category_factory()
        product_factory(category=obj1)
        with pytest.raises(IntegrityError):
            obj1.delete()

    def test_return_product_active_only_true(self, product_factory):
        product_factory(is_active=True)
        product_factory(is_active=False)
        qs = Product.objects.is_active().count()
        assert qs == 1

    def test_return_product_active_only_false(self, product_factory):
        product_factory(is_active=True)
        product_factory(is_active=False)
        qs = Product.objects.count()
        assert qs == 2
