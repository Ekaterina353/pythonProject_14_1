import unittest
from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):
    """
    Тесты для класса Category.
    """

    def setUp(self):
        """
        Настройка тестовой среды перед каждым тестом.
        """

        self.category = Category("Test Category", "Description for test category")
        self.product1 = Product("Product 1", "Description 1", 100.0)
        self.product2 = Product("Product 2", "Description 2", 200.0)

    def test_add_product(self):
        """
        Проверяет добавление продукта в категорию.
        """

        self.category.add_product(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.assertIn(self.product1, self.category.products)

    def test_average_price_empty_category(self):
        """
        Проверяет вычисление средней цены для пустой категории.
        """

        self.assertEqual(self.category.average_price(), 0.0)

    def test_average_price_non_empty_category(self):
        """
        Проверяет вычисление средней цены для непустой категории.
        """

        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        expected_average = (self.product1.price + self.product2.price) / 2
        self.assertEqual(self.category.average_price(), expected_average)

    def test_category_initialization(self):
        """
        Проверяет инициализацию класса Category.
        """

        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "Description for test category")
        self.assertEqual(self.category.products, [])


if __name__ == '__main__':
    unittest.main()
