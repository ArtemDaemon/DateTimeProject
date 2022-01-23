import json
from . import date_time as dt


class DateTimeContainer(object):
    def __init__(self):
        """Конструктор контейнера. Формирует пустой лист"""

        self.container = []

    def __str__(self):
        """Вывод индексов и значений элементов контейнера в читаемом виде"""

        string_result = ""
        for index, date_time in enumerate(self.container):
            string_result += f"{index} - {date_time}\n"
        return string_result

    def __getitem__(self, item):
        """Возвращение элемента списка"""

        try:
            return self.container[int(item)]
        except ValueError:
            print("Введите целочисленное значение индекса")
        except IndexError:
            print("Элемента с таким индексом нет")

    def add(self, date_time_object):
        """Добавление элемента в список"""

        if isinstance(date_time_object, dt.DateTime):
            self.container.append(date_time_object)
        else:
            print("Вы пытаетесь добавить объект, не подходящий для хранения в данном контейнере")

    def delete_by_index(self, index):
        """Удаление элемента по индексу"""

        try:
            del self.container[int(index)]
        except ValueError:
            print("Введите целочисленное значение индекса")
        except IndexError:
            print("Элемента с таким индексом нет")

    def delete_by_value(self, date_time_object):
        """Удаление элемента по значению (ссылке на объект)"""

        try:
            self.container.remove(int(date_time_object))
        except ValueError:
            print("Введите целочисленное значение индекса")
        except IndexError:
            print("Элемента с таким индексом нет")

    def json_save(self):
        """Сохранение словаря данных в JSON-файл"""

        with open('date_time_container.json', 'w', encoding='utf-8') as export_file:
            json.dump([date_time.__dict__ for date_time in self.container], export_file, indent=4)

    def json_load(self, path):
        """Загрузка словаря данных из JSON-файла"""

        try:
            with open(path, 'r', encoding='utf-8') as import_file:
                import_data = json.load(import_file)
            self.container.clear()
            empty_dict_set = {'_day': 1, '_month': 1, '_year': 2000, '_hour': 0, '_minute': 0}
            for date_time in import_data:
                date_time_object = dt.DateTime(dict_set=empty_dict_set)
                date_time_object.dict_load(date_time_object, date_time)
                self.container.append(date_time_object)
        except FileNotFoundError:
            print("Файл не найден")
