from src.product import Product


class Category:
    """
    Класс, представляющий категорию продуктов.
    """

    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализация экземпляра класса Category.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list, optional): Список продуктов в категории. Defaults to None.
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию.

        Args:
            product (Product): Продукт для добавления.
        """
        self.products.append(product)

    def average_price(self):
        """
        Вычисляет среднюю цену товаров в категории.

        Returns:
            float: Средняя цена товаров в категории. Возвращает 0, если категория пуста.
        """
        if not self.products:
            return 0.0
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0.0
