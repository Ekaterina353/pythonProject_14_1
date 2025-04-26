from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_product_attributes():
    """Тест атрибутов продукта через дочерние классы."""
    grass = LawnGrass("Green Grass", "Good grass", 100, 10, "Ryegrass", "Green")
    phone = Smartphone("SuperPhone", "Cool phone", 500, 5, "High", "ModelX", 128)

    assert grass.name == "Green Grass"
    assert phone.name == "SuperPhone"
