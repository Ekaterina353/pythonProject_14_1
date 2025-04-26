import unittest
from src.mixins import PrintableMixin
from src.base_product import BaseProduct
from src.product import Product


class TestProduct(unittest.TestCase):
    """Тесты для класса Product."""

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.product = Product("Test Product", "A test product", 10.0, 100)

    def test_product_inheritance(self):
        """Проверка наследования от PrintableMixin и BaseProduct."""
        self.assertIsInstance(self.product, PrintableMixin)
        self.assertIsInstance(self.product, BaseProduct)

    def test_product_initialization(self):
        """Проверка инициализации атрибутов продукта."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "A test product")
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.quantity, 100)

    def test_product_quantity_type(self):
        """Проверка, что количество является целым числом."""
        self.assertIsInstance(self.product.quantity, int)


if __name__ == '__main__':
    unittest.main()
