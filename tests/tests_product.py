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
