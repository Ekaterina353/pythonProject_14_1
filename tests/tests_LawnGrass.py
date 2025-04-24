from src.product import Product


class LawnGrass(Product):
    """Класс газонной травы, наследник Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int,
                 color: str):
        """
        Конструктор класса LawnGrass.

        :param name: Название газонной травы.
        :param description: Описание газонной травы.
        :param price: Цена за единицу.
        :param quantity: Количество в наличии.
        :param country: Страна производитель.
        :param germination_period: Срок прорастания (в днях).
        :param color: Цвет травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Возвращает строковое представление объекта LawnGrass."""
        return f"{super().__str__()}, Страна: {self.country}, Срок прорастания: {self.germination_period} дней, Цвет: {self.color}"
