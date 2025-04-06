class Product:
    """
    Класс, представляющий продукт.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта Product.

        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
