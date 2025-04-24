from src.product import Product


class Smartphone(Product):
    """Класс смартфона, наследник Product."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{super().__str__()} - {self.model}, {self.color}"
