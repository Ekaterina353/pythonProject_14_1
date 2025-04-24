class Product:
    """Базовый класс продукта."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        """Сложение продуктов одного класса."""
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных классов.")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. (Остаток: {self.quantity})"
