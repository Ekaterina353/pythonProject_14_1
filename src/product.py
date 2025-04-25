class Product:
    """Базовый класс продукта."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для приватной цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для приватной цены с валидацией."""
        if new_price <= 0:
            print("Цена должна быть больше нуля.")  # Вывод сообщения вместо исключения
        else:
            self.__price = new_price

    def __add__(self, other):
        """Сложение продуктов одного класса."""
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных классов.")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. (Остаток: {self.quantity})"

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """Классовый метод для создания нового продукта."""
        return cls(name, description, price, quantity)
