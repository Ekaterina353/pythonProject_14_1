import pytest
from main import LawnGrass
from src.product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания экземпляра Product."""
    return Product("Test Product", "Description", 100, 5)


def test_product_creation(sample_product):
    """Проверка создания объекта Product."""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Description"
    assert sample_product.price == 100
    assert sample_product.quantity == 5


def test_product_addition(sample_product):
    """Проверка сложения двух продуктов."""
    product2 = Product("Another Product", "Desc", 50, 10)
    assert sample_product.add(product2) == 100 * 5 + 50 * 10


def test_product_addition_different_types(sample_product):
    """Проверка исключения при сложении продуктов разных типов."""
    lawn_grass = LawnGrass("Grass", "Desc", 20, 20, "Russia", "2 weeks", "Green")
    with pytest.raises(TypeError):
        sample_product.add(lawn_grass)


def test_product_string_representation(sample_product):
    """Проверка строкового представления Product."""
    assert str(sample_product) == "Test Product, 100 руб. (Остаток: 5)"
