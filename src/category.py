from src.product import Product


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def get_products(self):
        """Возвращает информацию о продуктах в категории в виде строк."""
        return [str(product) for product in self.products]


# Пример использования
if __name__ == '__main__':
    product1 = Product("Яблоко", "Красное", 50, 100)
    product2 = Product("Груша", "Зеленая", 80, 50)

    category = Category("Фрукты", "Свежие фрукты", [product1, product2])

    print(product1)  # Вывод: Яблоко, 50 руб. Остаток: 100 шт.
    print(category)  # Вывод: Фрукты, количество продуктов: 150 шт.

    total_cost = product1 + product2
    print(f"Общая стоимость товаров: {total_cost}")  # Вывод: Общая стоимость товаров: 9000
