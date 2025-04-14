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
        self.__price = price
        self.quantity = quantity



@property
def price(self):
    """Геттер для получения цены."""
    return self.__price


@price.setter
def price(self, new_price: float):
    """Сеттер для установки цены с проверкой."""
    if new_price > 0:
        self.__price = new_price
    else:
        print("Цена не должна быть нулевая или отрицательная")
