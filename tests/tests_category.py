import unittest
from src.product import Product
from src.category import Category



class TestCategory(unittest.TestCase):

    def setUp(self):

        """
        Подготовка тестовых данных перед каждым тестом.
        """
        self.category = Category("Test Category", "Test Description")
        self.product1 = Product("Product 1", "Description 1", 100.0)
        self.product2 = Product("Product 2", "Description 2", 200.0)

    def test_category_creation(self):

        """
        Проверка корректности создания экземпляра Category.
        """
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "Test Description")
        self.assertEqual(self.category.products, [])

    def test_add_product(self):

        """
        Проверка добавления продукта в категорию.
        """
        self.category.add_product(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(self.category.products[0], self.product1)

    def test_average_price_empty_category(self):

        """
        Проверка вычисления средней цены для пустой категории.
        """
        self.assertEqual(self.category.average_price(), 0.0)

    def test_average_price_non_empty_category(self):

        """
        Проверка вычисления средней цены для непустой категории.
        """
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(self.category.average_price(), 150.0)


if __name__ == '__main__':
    unittest.main()
