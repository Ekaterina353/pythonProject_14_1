from src.mixins import PrintableMixin
from src.base_product import BaseProduct


class Product(PrintableMixin, BaseProduct):
    """Класс для представления продукта."""

    def __init__(self, name, description, price, quantity):
        """Инициализация продукта."""
        super().__init__(name, description, price, quantity)
