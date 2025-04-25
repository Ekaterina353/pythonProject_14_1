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
