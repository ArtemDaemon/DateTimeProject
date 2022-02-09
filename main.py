import sys

from date_time_package import date_time as dt
from date_time_package import date_time_container as dtc
from date_time_package import examples as examples

menu_login = {
    0: "Выберите режим работы с программой",
    1: ("Режим пользователя", "menu_user"),
    2: ("Режим администратора", "menu_admin"),
    3: ("Выход", "exit")}
menu_user = {
    0: "Режим пользователя. Реализация класса Дата/Время.",
    1: ("Работа с классом Дата/Время", "choose_date_time"),
    2: ("Загрузка примеров", "run_examples"),
    3: ("Назад", "menu_login")}
menu_json_save_user = {
    0: "Желаете сохранить объект в JSON?",
    1: ("Да", "json_save_dt"),
    2: ("Нет", "exit")}
menu_admin = {
    0: "Режим администратора. "
       "Реализация классов Дата/Время и контейнера",
    1: ("Работа с классом Дата/Время", "menu_create_dt_admin"),
    2: ("Работа с классом контейнера объектов Дата/Время",
        "menu_container"),
    3: ("Назад", "menu_login")}
menu_create_dt_admin = {
    0: "Создание объекта  Дата/Время.",
    1: ("Создание объекта из набора данных",
        "create_date_time_dict"),
    2: ("Создание объекта из строки",
        "create_date_time_str"),
    3: ("Назад", "menu_admin")}
menu_dt_admin = {
    0: "Работа с классом Дата/Время",
    1: ("Сохранение данных в JSON", "json_save_dt"),
    2: ("Загрузка данных из JSON", "json_load_dt"),
    3: ("Назад", "exit")}
menu_container = {
    0: "Работа с контейнером",
    1: ("Удалить объект Дата/Время", "container_del"),
    2: ("Изменить объект в контейнере", "container_change"),
    3: ("Сохранить в JSON", "container_save"),
    4: ("Загрузить из JSON", "container_load"),
    5: ("Назад", "menu_admin")}


def main():
    """Главный метод программы"""

    menu = menu_login
    menu_key = -1
    menu_option = ""

    date_time_base = dtc.DateTimeContainer()
    date_time_example = dt.DateTime("21.07.1998 21:46")
    date_time_base.add(date_time_example)

    choose_menu(menu, menu_key, menu_option, date_time_base)


def choose_menu(menu, menu_key, menu_option, metadata):
    """Считывание выбранного пункта меню

    Если пункт меню указывает на словарь, его значение отправляется
    для отображения нового меню. Если пункт меню указывает на функцию,
    вцызывается функция с данным названием
    """

    while menu_option != "exit":
        if menu_key > -1 and \
                menu_option in [value[1] for value in menu.values()]:

            executable_object = getattr(sys.modules[__name__], menu_option)

            if type(executable_object) == dict:
                (menu, menu_key, menu_option) = \
                    display_menu(executable_object)
            else:
                executable_object(metadata)
                menu_key = -1
        else:
            (menu, menu_key, menu_option) = display_menu(menu)


def display_menu(menu_dict):
    """Вывод пунктов меню, проверка вводимого ответа"""

    menu_list = []
    while len(menu_list) == 0:
        print('{0:^9}'.format(menu_dict[0]))

        for key in sorted(menu_dict.keys()):
            if key >= 1:
                print('{0: <9} {1: <30}'.format(key, menu_dict[key][0]))
        try:
            choice = int(input("\nПожалуйста выберите пункт меню... "))
            if choice in menu_dict and choice >= 1:
                menu_list = menu_dict, choice, menu_dict[choice][1]
        except ValueError:
            print("Введен некорректный ответ")

    return menu_list


def choose_date_time(date_time_base):
    """Выбор индекса объекта в контейнере для работы с ним"""

    date_time_object = None
    while date_time_object is None:
        print(
            f"Список созданных объектов:\n{date_time_base.__str__()}\n"
            "Введите индекс объекта, с которым хотите работать")
        index = input()
        date_time_object = date_time_base.__getitem__(index)

    choose_menu(menu_json_save_user, -1, "", date_time_object)


def json_save_dt(date_time_object):
    """Сохранение выбранного объекта Дата/Время в JSON"""

    date_time_object.json_save()
    print("Объект сохранен в локальную папку в файл date_time.json")


def json_load_dt(date_time_object):
    """Загрузка данных объекта Дата/Время из JSON"""

    filepath = input(
        "Введите относительный или абсолютный адрес сохранения файла ")
    date_time_object.json_load(filepath)


def run_examples(metadata):
    """Запуск примеров"""

    examples.run()


def create_date_time_dict(date_time_base):
    """Создание объекта Дата/Время из данных вводимого словаря """

    day = input("День: ")
    month = input("Месяц: ")
    year = input("Год: ")
    hour = input("Час: ")
    minute = input("Минута: ")
    data = {
        '_day': day, '_month': month, '_year': year,
        '_hour': hour, '_minute': minute}
    date_time_object = dt.DateTime(dict_set=data)
    date_time_base.add(date_time_object)
    choose_menu(menu_dt_admin, -1, "", date_time_object)


def create_date_time_str(date_time_base):
    """Создание объекта Дата/Время из данных строки"""

    data = input(
        "Маска для ввода дд.мм.гг ЧЧ:ММ например, 21.07.1998 21:47  ")
    date_time_object = dt.DateTime(string_set=data)
    date_time_base.add(date_time_object)
    choose_menu(menu_dt_admin, -1, "", date_time_object)


def container_del(date_time_base):
    """Удаление объекта из контейнера по его индексу"""

    print(f"Список объектов контейнера:\n{date_time_base.__str__()}\n")
    index = input("Введите индекс объекта, который хотите удалить ")
    date_time_base.delete_by_index(index)


def container_change(date_time_base):
    """Изменение данных объекта Дата/Время в контейнере"""

    print(f"Список объектов контейнера:\n{date_time_base.__str__()}\n")
    index = input("Введите индекс объекта, который хотите изменить ")
    date_time_object = date_time_base.__getitem__(index)
    date_time_object.day = input("День: ")
    date_time_object.month = input("Месяц: ")
    date_time_object.year = input("Год: ")
    date_time_object.hour = input("Час: ")
    date_time_object.minute = input("Минута: ")


def container_save(date_time_base):
    """Сохранение контейнера в JSON"""

    date_time_base.json_save()
    print(
        "Контейнер сохранен в локальную папку в файл"
        "date_time_container.json")


def container_load(date_time_base):
    """Загрузка данных контейнера из JSON"""

    filepath = input(
        "Введите относительный или абсолютный адрес сохранения файла ")
    date_time_base.json_load(filepath)


if __name__ == '__main__':
    sys.exit(main())
