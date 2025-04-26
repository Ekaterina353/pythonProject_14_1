from src.product import Product


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name, description, price, quantity, type_grass, color):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.type_grass = type_grass
        self.color = color
