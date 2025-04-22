import pytest
from main import Smartphone, LawnGrass, Category

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
