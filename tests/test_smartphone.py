from src.product import Product


class Smartphone(Product):
    """Класс смартфона, наследник Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str,
                 memory: int, color: str):
        """
        Конструктор класса Smartphone.

        :param name: Название смартфона.
        :param description: Описание смартфона.
        :param price: Цена.
        :param quantity: Количество в наличии.
        :param efficiency: Процессор.
        :param model: Модель смартфона.
        :param memory: Объем памяти (ГБ).
        :param color: Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Возвращает строковое представление объекта Smartphone."""
        return f"{super().__str__()}, Модель: {self.model}, Цвет: {self.color}"
