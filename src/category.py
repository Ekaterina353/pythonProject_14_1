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
        self.__products = products  # Приватный атрибут списка товаров
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        """Геттер для получения информации о товарах."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def add_product(self, new_product: Product):
        """
        Метод для добавления продукта в категорию.
        Проверяет, является ли добавляемый объект экземпляром класса Product.
        """
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты типа Product")

    def __str__(self):
        return f"Category: {self.name}, Products: {len(self.__products)}"
