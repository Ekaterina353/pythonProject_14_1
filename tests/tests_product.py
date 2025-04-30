import pytest
from src.product import Product  # Замените your_module на имя вашего файла


def test_product_creation():
    """
    Тест проверяет успешное создание экземпляра Product.
    """
    product = Product("Test Product", "Test Description", 99.99, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 99.99
    assert product.quantity == 10


def test_product_creation_with_zero_quantity():
    """
    Тест проверяет, что ValueError возникает при создании Product с quantity = 0.
    """
    with pytest.raises(ValueError) as excinfo:
        Product("Test Product", "Test Description", 99.99, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_product_str_representation():
    """
    Тест проверяет строковое представление объекта Product.
    """
    product = Product("Test Product", "Test Description", 99.99, 10)
    assert str(product) == "Test Product, 99.99 руб. Остаток: 10 шт."
