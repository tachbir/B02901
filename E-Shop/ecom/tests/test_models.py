import pytest
from ecom.models import Product

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(name='Test Product', price=99.99, stock=10)
    assert product.name == 'Test Product'
    assert product.price == 99.99
    assert product.stock == 10
