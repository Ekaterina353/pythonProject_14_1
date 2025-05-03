import pytest
from src.product import Product


def test_product_creation():
    """Проверяет создание экземпляра Product."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str():
    """Проверяет строковое представление Product."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_zero_quantity():
    """Проверяет исключение при нулевом количестве."""
    with pytest.raises(ValueError):
        Product("Test Product", "Test Description", 100.0, 0)
