from . import date_time as dt
from . import date_time_container as dtc


def run():
    """Запуск примеров"""

    # Пример 1 - Создание date_time на основе dict
    print("Пример 1 - Создание объекта Дата/Время на основе словаря")
    example1_dict = {
        '_day': 21,
        '_month': 7,
        '_year': 1998,
        '_hour': 21,
        '_minute': 48}
    print(f"Данные словаря:\n{example1_dict}")
    example1_date_time = dt.DateTime(dict_set=example1_dict)
    print(example1_date_time)

    # Пример 2 - Создание date_time на основе string
    print("\nПример 2 - Создание объекта Дата/Время на основе строки")
    example2_str = "24.03.1967 21:54"
    print(f"Данные строки: {example2_str}")
    example2_date_time = dt.DateTime(string_set=example2_str)
    print(example2_date_time)

    # Пример 3 - Попытка создание date_time с неправильными данными
    print(
        "Пример 3 - Попытка создания объекта Дата/Время на основе словаря с"
        "некорректными данными")
    wrong_example_dict = {
        '_day': 32,
        '_month': -17,
        '_year': '1998',
        '_hour': None,
        '_minute': 6000}
    print(f"Данные словаря:\n{wrong_example_dict}")
    wrong_example_date_time = dt.DateTime(dict_set=wrong_example_dict)
    print(wrong_example_date_time)

    # Пример 4 - Создание date_time_container
    print(
        "\nПример 4 - Создание контейнера для созданных раннее объектов"
        "Дата/Время")
    example3_date_time_container = dtc.DateTimeContainer()
    example3_date_time_container.add(example1_date_time)
    example3_date_time_container.add(example2_date_time)
    print(example3_date_time_container)

    # Пример 5 - Сохранение и загрузка JSON для date_time
    print(
        "\nПример 5 - Сохранение первого созданного объекта Дата/Время в"
        "JSON и загрузка данных во второй")
    example1_date_time.json_save()
    example2_date_time.json_load("date_time.json")
    print(example3_date_time_container)
