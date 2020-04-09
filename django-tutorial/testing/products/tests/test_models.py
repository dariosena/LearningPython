import pytest

from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:

    def test_product_is_in_stock(self):
        product = mixer.blend('products.Product', quantity=1)
        assert product.is_in_stock == True
        
    def test_product_is_not_in_stock(self):
        product = mixer.blend('products.Product', quantity=0)
        assert product.is_in_stock == False

