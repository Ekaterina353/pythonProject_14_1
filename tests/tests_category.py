
=======
import pytest

from main import Smartphone, LawnGrass

def test_product_addition():
    """Тест сложения продуктов одного класса."""
    phone1 = Smartphone("Samsung", "хороший", 10000, 2, "Высокая", "S23", 256, "Black")
    phone2 = Smartphone("Apple", "тоже хороший", 12000, 3, "Очень высокая", "iPhone 15", 512, "White")
    assert phone1 + phone2 == 56000

def test_product_addition_error():
    """Тест на ошибку при сложении продуктов разных классов."""
    phone = Smartphone("Samsung", "хороший", 10000, 2, "Высокая", "S23", 256, "Black")
    grass = LawnGrass("Зеленая", "отличная", 500, 10, "Россия", "14 дней", "Зеленый")
    with pytest.raises(TypeError):
        phone + grass
=======
from src.product import Product
from src.category import Category



def test_category_creation():
    """Проверяет создание экземпляра класса Category."""
    product1 = Product("Product 1", "Description 1", 50, 10)
    product2 = Product("Product 2", "Description 2", 25, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == [product1, product2]

def test_category_string_representation():
    """Проверяет строковое представление экземпляра класса Category."""
    product1 = Product("Product 1", "Description 1", 50, 10)
    product2 = Product("Product 2", "Description 2", 25, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert str(category) == "Test Category, количество продуктов: 30 шт."

def test_category_get_products():
    """Проверяет метод get_products класса Category."""
    product1 = Product("Product 1", "Description 1", 50, 10)
    product2 = Product("Product 2", "Description 2", 25, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    products_info = category.get_products()
    assert products_info == ["Product 1, 50 руб. Остаток: 10 шт.", "Product 2, 25 руб. Остаток: 20 шт."]
=======
@pytest.fixture
def sample_product():
    """Фикстура для создания экземпляра Product."""
    return Product("Test Product", "Test Description", 100.0, 5)


@pytest.fixture
def sample_category(sample_product):
    """Фикстура для создания экземпляра Category."""
    return Category("Test Category", "Test Category Description", [sample_product])


def test_category_creation(sample_category, sample_product):
    """Тест проверяет создание экземпляра Category и его атрибуты."""
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_products_property(sample_category, sample_product):
    """Тест проверяет геттер products."""
    expected_output = f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт.\n"
    assert sample_category.products == expected_output


def test_category_str(sample_category):
    """Тест проверяет метод __str__."""
    assert str(sample_category) == "Category: Test Category, Products: 1"


def test_category_count_increment():
    """Тест проверяет увеличение category_count."""
    Category.category_count = 0  # Сброс счетчика
    category1 = Category("Category 1", "Description 1", [])
    category2 = Category("Category 2", "Description 2", [])
    assert Category.category_count == 2


def test_product_count_increment(sample_product):
    """Тест проверяет увеличение product_count."""
    Category.product_count = 0  # Сброс счетчика
    product2 = Product("Test Product 2", "Test Description 2", 50.0, 10)
    category = Category("Category with multiple products", "Description", [sample_product, product2])
    assert Category.product_count == 2

