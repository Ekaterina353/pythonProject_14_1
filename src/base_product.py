from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для продуктов."""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
