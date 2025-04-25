from src.product import Product


class Category:
    """Класс категории продуктов."""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут

    @property
    def products(self):
        """Геттер для приватного списка продуктов."""
        return self.__products

    def add_product(self, product):
        """Добавление продукта в категорию с проверкой типа."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product и его наследников.")
        self.__products.append(product)

    def __str__(self):
        product_list = "\n".join([str(product) for product in self.products])
        return f"{self.name}, {self.description}\n{product_list}\n"
