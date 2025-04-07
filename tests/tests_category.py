import pytest
import unittest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Category Description", [sample_product])


class TestCategory(unittest.TestCase):
    """
    Тесты для класса Category.
    """

    def setUp(self):
        """
        Подготовка к каждому тесту: сброс счетчиков категорий и продуктов, создание тестовых продуктов.
        """
        Category.category_count = 0
        Category.product_count = 0
        self.product1 = Product("Test Product 1", "Description 1", 100, 5)
        self.product2 = Product("Test Product 2", "Description 2", 200, 10)
        self.products = [self.product1, self.product2]

    def test_category_creation(self):
        """
        Тест создания объекта Category и проверки его атрибутов.
        """
        category = Category("Test Category", "Test Description", self.products)
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test Description")
        self.assertEqual(category.products, self.products)
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 2)

    def test_category_creation_no_products(self):
        """
        Тест создания объекта Category без продуктов.
        """
        category = Category("Empty Category", "No products here", [])
        self.assertEqual(category.name, "Empty Category")
        self.assertEqual(category.description, "No products here")
        self.assertEqual(category.products, [])
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 0)

    def test_str_representation(self):
        """
        Тест строкового представления объекта Category.
        """
        category = Category("Test Category", "Test Description", self.products)
        self.assertEqual(str(category), "Category: Test Category, Products: 2")

    def test_empty_product_list(self):
        """
        Тест с пустой списком продуктов
        """
        category = Category("Empty Category", "No products", [])
        self.assertEqual(str(category), "Category: Empty Category, Products: 0")


def test_category_creation(sample_product, sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Test Product"


if __name__ == '__main__':
    unittest.main()
