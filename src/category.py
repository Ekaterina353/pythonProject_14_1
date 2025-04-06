from src.product import Product


class Category:
    """
    Класс, представляющий категорию продуктов.
    """
    category_count = 0  # Атрибут класса: общее количество категорий
    product_count = 0  # Атрибут класса: общее количество продуктов

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории (объекты Product).
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f"Category: {self.name}, Products: {len(self.products)}"
