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
