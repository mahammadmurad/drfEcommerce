from drfEcommerce.product.models import *

class TestCategoryModel:
    def test_str_method_(self, category_factory):
        x = category_factory.get_category()
        assert x.__str__() == 'test_category'


class TestBrandModel:
    pass


class TestProductModel:
    pass
