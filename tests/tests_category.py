import pytest
from src.category import  Category


@pytest.fixture
def sample_category():
    """Фикстура для создания экземпляра Category."""
    return Category("Test Category", "Category Description")


def test_category_creation(sample_category):
    """Проверка создания объекта Category."""
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Category Description"
    assert sample_category.products == []


def test_category_add_product(sample_category, sample_product):
    """Проверка добавления продукта в категорию."""
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_add_invalid_product(sample_category):
    """Проверка исключения при добавлении некорректного типа продукта."""
    with pytest.raises(TypeError):
        sample_category.add_product("Not a Product")


def test_category_string_representation(sample_category, sample_product):
    """Проверка строкового представления Category."""
    sample_category.add_product(sample_product)
    expected_string = f"Test Category, Category Description\n{str(sample_product)}\n"
    assert str(sample_category) == expected_string
