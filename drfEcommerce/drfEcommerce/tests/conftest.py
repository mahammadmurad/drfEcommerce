from pytest_factoryboy import register
from . factories import CategoryFactory, BrandFactory
import pytest_
from rest_framework.test import APIClient

register(CategoryFactory)
register(BrandFactory)


@pytest.fixture
def api_client():
    return APIClient
