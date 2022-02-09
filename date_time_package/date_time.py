import json
import datetime


class DateTime:
    """Класс Дата/Время"""

    def __init__(self, string_set=None, dict_set=None):
        """Конструктор принимающий или строку или словарь"""

        if string_set is not None:
            self._day, self._month, self._year, self._hour, self._minute = \
                DateTime.convert_string(string_set)
        else:
            DateTime.dict_load(self, dict_set)

    def __str__(self):
        """Вывод данных объекта в читаемом виде

        Если значение меньше двухзначного (кроме года),
        добавляется ноль
        """

        temp_day = self.add_zero(self._day)
        temp_month = self.add_zero(self._month)
        temp_hour = self.add_zero(self._hour)
        temp_minute = self.add_zero(self._minute)

        return f'{temp_day}.{temp_month}.{self._year} ' \
               f'{temp_hour}:{temp_minute}'

    @staticmethod
    def convert_string(string_set):
        """Деление строки на части"""

        try:
            date, time = string_set.split()
            day, month, year = list(map(int, date.split(".")))
            hour, minute = list(map(int, time.split(":")))
            datetime.datetime(
                day=day, month=month, year=year, hour=hour, minute=minute)
            return [day, month, year, hour, minute]
        except ValueError:
            print("Введён неправильный формат объекта Дата/Время")
            return [1, 1, 2000, 0, 0]

    @staticmethod
    def dict_load(self, dict_set):
        """Метод для загрузки данных их словаря.

        Проверяет на корректность
        значений, а также на соответствие ключей, когда словарь
        загружается из JSON-файла"""

        try:
            self._day = int(dict_set["_day"])
            self._month = int(dict_set["_month"])
            self._year = int(dict_set["_year"])
            self._hour = int(dict_set["_hour"])
            self._minute = int(dict_set["_minute"])
            datetime.datetime(
                day=self._day, month=self._month, year=self._year,
                hour=self._hour, minute=self._minute)
        except ValueError:
            print("Введён неправильный формат объекта Дата/Время")
            self._day, self._month, self._year, self._hour, self._minute = \
                1, 1, 2000, 0, 0
        except TypeError:
            print("Введён неправильный формат объекта Дата/Время")
            self._day, self._month, self._year, self._hour, self._minute = \
                1, 1, 2000, 0, 0
        except KeyError:
            print("JSON-файл содержит неправильные ключи")

    @staticmethod
    def add_zero(variable):
        """Добавление нуля к началу односимвольных значений"""
        if variable < 10:
            return "0" + str(variable)
        else:
            return variable

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        try:
            datetime.datetime(
                day=int(value), month=self._month, year=self._year)
            self._day = int(value)
        except ValueError:
            print("Введено некорректное значение")
        except TypeError:
            print("Введено некорректное значение")

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        try:
            if 1 <= int(value) <= 12:
                self._month = int(value)
            else:
                raise ValueError
        except ValueError:
            print("Введено некорректное значение")
        except TypeError:
            print("Введено некорректное значение")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        try:
            if 1 <= int(value) <= 2500:
                self._year = int(value)
            else:
                raise ValueError
        except ValueError:
            print("Введено некорректное значение")
        except TypeError:
            print("Введено некорректное значение")

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        try:
            if 0 <= int(value) <= 23:
                self._hour = int(value)
            else:
                raise ValueError
        except ValueError:
            print("Введено некорректное значение")
        except TypeError:
            print("Введено некорректное значение")

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        try:
            if 0 <= int(value) <= 60:
                self._minute = int(value)
            else:
                raise ValueError
        except ValueError:
            print("Введено некорректное значение")
        except TypeError:
            print("Введено некорректное значение")

    def json_save(self):
        """Сохраняет словарь данных объекта в JSON-файл"""

        with open('date_time.json', 'w', encoding='utf-8') as export_file:
            json.dump(self.__dict__, export_file, indent=4)

    def json_load(self, path):
        """Загружает словарь данных из JSON-файла"""

        try:
            with open(path, 'r', encoding='utf-8') as import_file:
                import_data = json.load(import_file)
            DateTime.dict_load(self, import_data)
        except FileNotFoundError:
            print("Файл не найден")
