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
