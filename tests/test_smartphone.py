from src.smartphone import Smartphone


def test_smartphone_creation(capsys):
    """Тест создания объекта Smartphone и атрибутов."""
    phone = Smartphone("SuperPhone", "Cool phone", 500, 5, "High", "ModelX", 128)
    assert phone.name == "SuperPhone"
    assert phone.description == "Cool phone"
    assert phone.price == 500
    assert phone.quantity == 5
    assert phone.performance == "High"
    assert phone.model == "ModelX"
    assert phone.memory == 128
    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone" in captured.out
