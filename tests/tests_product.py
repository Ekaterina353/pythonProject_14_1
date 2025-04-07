import unittest
from main import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """
        Настройка тестовых данных перед каждым тестом.
        """
        self.product1 = Product("Test Product", "A test product description", 10.0, 100)
        self.product2 = Product("Another Product", "Another description", 25.50, 50)
        self.product3 = Product("Expensive Item", "A high-value item", 100.0, 5)
        self.product4 = Product("Cheap Item", "A low-cost item", 1.0, 1000)
        self.product5 = Product("Zero Quantity", "Item with no stock", 50.0, 0)

    def test_product_name(self):
        """
        Проверка изменения имени продукта
        """
        self.product1.name = "New Name"
        self.assertEqual(self.product1.name, "New Name")

    def test_product_description(self):
        """
        Проверка изменения описания продукта
        """
        self.product1.description = "New Description"
        self.assertEqual(self.product1.description, "New Description")

    def test_product_price(self):
        """
        Проверка изменения цены продукта
        """
        self.product1.price = 15.0
        self.assertEqual(self.product1.price, 15.0)

    def test_product_quantity(self):
        """
        Проверка изменения количества продукта
        """
        self.product1.quantity = 50
        self.assertEqual(self.product1.quantity, 50)

    def test_product_str(self):
        """
        Проверяет корректность строкового представления объекта Product.
        """
        expected_string = "Product: Test Product, Price: 10.0, Quantity: 100"
        self.assertEqual(str(self.product1), expected_string)

        expected_string = "Product: Another Product, Price: 25.5, Quantity: 50"
        self.assertEqual(str(self.product2), expected_string)

    def test_product_different_values(self):
        """
        Проверяет, что продукты с разными значениями инициализируются правильно.
        """
        self.assertEqual(self.product3.price, 100.0)
        self.assertEqual(self.product3.quantity, 5)

        self.assertEqual(self.product4.price, 1.0)
        self.assertEqual(self.product4.quantity, 1000)

    def test_product_zero_quantity(self):
        """
        Проверяет создание продукта с нулевым количеством.
        """
        self.assertEqual(self.product5.quantity, 0)


if __name__ == '__main__':
    unittest.main()
