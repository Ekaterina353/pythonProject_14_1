class PrintableMixin:
    """Миксин для вывода информации о созданном объекте."""

    def __init__(self, *args, **kwargs):
        """Выводит информацию о классе и параметрах при создании объекта."""
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ", ".join(
            [repr(arg) for arg in args] + [f"{key}={repr(value)}" for key, value in kwargs.items()]
        )
        print(f"Создан объект класса {class_name} с параметрами: {params}")
