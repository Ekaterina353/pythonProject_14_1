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
