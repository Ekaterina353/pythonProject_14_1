from src.lawngrass import LawnGrass


def test_lawn_grass_creation(capsys):
    """Тест создания объекта LawnGrass и атрибутов."""
    grass = LawnGrass("Green Grass", "Good grass", 100, 10, "Ryegrass", "Green")
    assert grass.name == "Green Grass"
    assert grass.description == "Good grass"
    assert grass.price == 100
    assert grass.quantity == 10
    assert grass.type_grass == "Ryegrass"
    assert grass.color == "Green"
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out
