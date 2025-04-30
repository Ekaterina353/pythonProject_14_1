class Product:
    """
    Класс, представляющий продукт.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация экземпляра класса Product.

        Args:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта.

        Raises:
            ValueError: Если количество товара равно нулю.
        """
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
