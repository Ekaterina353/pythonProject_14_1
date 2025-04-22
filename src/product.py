
class Product:

    """Базовый класс продукта."""
    def __init__(self, name, description, price, quantity):
=======
    def __init__(self, name, description, price, quantity):
=======
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
        self.__price = price
        self.quantity = quantity

    def __add__(self, other):
        """Сложение продуктов одного класса."""
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных классов.")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):

        return f"{self.name}, {self.price} руб. (Остаток: {self.quantity})"
=======
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение двух продуктов (возвращает общую стоимость)."""
        return (self.price * self.quantity) + (other.price * other.quantity)
=======
    @property
    def price(self):
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для установки цены с проверкой."""
        if isinstance(new_price, (int, float)):  # Проверяем тип данных
            if new_price > 0:
                self.__price = new_price
            else:
                print("Цена не должна быть нулевая или отрицательная")
        else:
            print("Цена должна быть числом")


