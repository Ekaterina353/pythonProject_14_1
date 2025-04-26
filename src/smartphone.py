from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(self, name, description, price, quantity, performance, model, memory):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
