
import pytest
from main import Smartphone, LawnGrass, Category


def test_category_add_product():
    """Тест добавления продукта в категорию."""
    category = Category("Телефоны", "Описание")
    phone = Smartphone("Samsung", "хороший", 10000, 2, "Высокая", "S23", 256, "Black")
    category.add_product(phone)
    assert len(category.products) == 1

def test_category_add_product_error():
    """Тест на ошибку при добавлении некорректного объекта в категорию."""
    category = Category("Телефоны", "Описание")
    with pytest.raises(TypeError):
        category.add_product("Строка")
=======

from src.product import Product

def test_product_creation():
    """Проверяет создание экземпляра класса Product."""
    product = Product("Test Product", "Test Description", 100, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100
    assert product.quantity == 10

def test_product_string_representation():
    """Проверяет строковое представление экземпляра класса Product."""
    product = Product("Test Product", "Test Description", 100, 10)
    assert str(product) == "Test Product, 100 руб. Остаток: 10 шт."

def test_product_addition():
    """Проверяет операцию сложения двух продуктов."""
    product1 = Product("Product 1", "Description 1", 50, 10)
    product2 = Product("Product 2", "Description 2", 25, 20)
    assert product1 + product2 == (50 * 10) + (25 * 20)
=======
import unittest
from src.product import Product  # Замените your_module на имя вашего файла

def test_product_creation():
    """Проверяет успешное создание экземпляра Product."""
    product = Product("Test Product", "A test product", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "A test product"
    assert product.price == 100.0
    assert product.quantity == 10

def test_price_getter():
    """Проверяет геттер цены."""
    product = Product("Test Product", "A test product", 100.0, 10)
    assert product.price == 100.0

def test_price_setter_valid():
    """Проверяет сеттер цены с валидным значением."""
    product = Product("Test Product", "A test product", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0

def test_price_setter_invalid(capsys):
    """Проверяет сеттер цены с невалидным значением."""
    product = Product("Test Product", "A test product", 100.0, 10)
    product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0  # Убеждаемся, что цена не изменилась

class TestProduct(unittest.TestCase):
    def test_price_setter_valid(self):
        product = Product("Test Product", "Description", 100.0, 10)
        product.price = 150.0
        self.assertEqual(product.price, 150.0)

    def test_price_setter_invalid_negative(self):
        product = Product("Test Product", "Description", 100.0, 10)
        product.price = -50.0
        self.assertEqual(product.price, 100.0)  # Цена не должна меняться

    def test_price_setter_invalid_type(self):
        product = Product("Test Product", "Description", 100.0, 10)
        product.price = "abc"
        self.assertEqual(product.price, 100.0)

