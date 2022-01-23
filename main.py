from date_time_package import date_time as dt
from date_time_package import date_time_container as dtc
from date_time_package import examples

if __name__ == '__main__':
    date_time_base = dtc.DateTimeContainer()

    """Выбор пользователя"""

    while True:
        print("Выберите режим работы с программой:\n"
              "1 - Режим пользователя\n"
              "2 - Режим администратора")
        key = input()
        if key == "1":

            """Режим пользователя"""

            while True:
                print("Реализация класса Дата/Время и контейнера для их хранения.\n"
                      "Выберите пункт меню:\n"
                      "1 - Работа с классом Дата/Время\n"
                      "2 - Загрузка примеров\n"
                      "3 - Назад")
                key = input()
                if key == "1":

                    """Пользователь -> Работа с классом Дата/Время"""

                    print(f"Список созданных объектов Дата/Время:\n{date_time_base.__str__()}\n"
                          "Введите индекс объекта, с которым хотите работать")
                    index = input()
                    date_time_object = date_time_base.__getitem__(index)
                    if date_time_object is None:
                        continue
                    while True:
                        print(f"Вы работаете с объектом - {date_time_object}")
                        print("Работа с классом Дата/Время. Выберите пункт меню:\n"
                              "1 - Сохранение данных в JSON\n"
                              "2 - Назад")
                        key = input()

                        if key == "1":

                            """Пользователь -> Работа с классом Дата/Время -> Сохранение данных в JSON"""

                            date_time_base.__getitem__(index).json_save()
                            print("Объект сохранен в локальную папку в файл date_time.json")
                        elif key == "2":
                            break

                elif key == "2":

                    """Пользователь -> Загрузка примеров"""

                    examples.run()
                elif key == "3":
                    break
        elif key == "2":

            """Режим администратора"""

            while True:
                print("Реализация класса Дата/Время и контейнера для их хранения.\n"
                      "Выберите пункт меню:\n"
                      "1 - Работа с классом Дата/Время\n"
                      "2 - Работа с классом контейнера объектов Дата/Время\n"
                      "3 - Назад")
                key = input()
                if key == "1":

                    """Администратор -> Работа с классом Дата/Время"""

                    while True:
                        print("Работа с классом Дата/Время. Выберите пункт меню:\n"
                              "1 - Создание объекта класса Дата/Время из набора данных\n"
                              "2 - Создание объекта класса Дата/Время из строк\n"
                              "3 - Назад")
                        key = input()
                        if key == "1" or key == "2":
                            if key == "1":

                                """Администратор -> Работа с классом Дата/Время -> Создание объекта из словаря"""

                                print("День:")
                                day = input()
                                print("Месяц:")
                                month = input()
                                print("Год:")
                                year = input()
                                print("Час:")
                                hour = input()
                                print("Минута:")
                                minute = input()
                                data = {'_day': day, '_month': month, '_year': year, '_hour': hour, '_minute': minute}
                                date_time_object = dt.DateTime(dict_set=data)
                                date_time_base.add(date_time_object)

                            elif key == "2":

                                """Администратор -> Работа с классом Дата/Время -> Создание объекта из строки"""

                                print("Маска для ввода дд.мм.гг ЧЧ:ММ например, 21.07.1998 21:47")
                                data = input()
                                date_time_object = dt.DateTime(string_set=data)
                                date_time_base.add(date_time_object)

                            while True:
                                print(f"Вы работаете с объектом - {date_time_object}")
                                print("Работа с классом Дата/Время. Выберите пункт меню:\n"
                                      "1 - Сохранение данных в JSON\n"
                                      "2 - Загрузка данных из JSON\n"
                                      "3 - Назад")
                                key = input()

                                if key == "1":

                                    """Администратор -> Работа с классом Дата/Время -> Сохранение данных в JSON"""

                                    date_time_object.json_save()
                                    print("Объект сохранен в локальную папку в файл date_time.json")
                                elif key == "2":

                                    """Администратор -> Работа с классом Дата/Время -> Загрузка данных из JSON"""

                                    print("Введите относительный или абсолютный адрес сохранения файла")
                                    filepath = input()
                                    date_time_object.json_load(filepath)
                                elif key == "3":
                                    break
                        elif key == "3":
                            break
                elif key == "2":

                    """Администратор -> Работа с классом контейнера объектов Дата/Время"""

                    while True:
                        print(f"Список созданных объектов Дата/Время:\n{date_time_base.__str__()}\n")

                        print("Выберите пункт меню:\n"
                              "1 - Добавить объект Дата/Время\n"
                              "2 - Удалить объект Дата/Время\n"
                              "3 - Изменить объект в контейнере\n"
                              "4 - Сохранить в JSON\n"
                              "5 - Загрузить из JSON\n"
                              "6 - Назад")
                        key = input()

                        if key == "1":

                            """Администратор -> Контейнер -> Добавить объект"""

                            while True:
                                print("Добавление объекта Дата/Время. Выберите пункт меню:\n"
                                      "1 - Создание объекта класса Дата/Время из набора данных\n"
                                      "2 - Создание объекта класса Дата/Время из строк\n"
                                      "3 - Назад")
                                key = input()
                                if key == "1" or key == "2":
                                    if key == "1":

                                        """Администратор -> Контейнер -> Добавить -> Создание объекта из словаря"""

                                        print("День:")
                                        day = input()
                                        print("Месяц:")
                                        month = input()
                                        print("Год:")
                                        year = input()
                                        print("Час:")
                                        hour = input()
                                        print("Минута:")
                                        minute = input()
                                        data = {'day': day, 'month': month, 'year': year, 'hour': hour,
                                                'minute': minute}
                                        date_time_object = dt.DateTime(dict_set=data)

                                    elif key == "2":

                                        """Администратор -> Контейнер -> Добавить -> Создание объекта из строки"""

                                        print("Маска для ввода дд.мм.гг ЧЧ:ММ например, 21.07.1998 21:47")
                                        data = input()
                                        date_time_object = dt.DateTime(string_set=data)

                                    date_time_base.add(date_time_object)
                                elif key == "3":
                                    break
                        elif key == "2":

                            """Администратор -> Контейнер -> Удалить объект Дата/Время"""

                            print("Введите индекс (начиная с 0) элемента, который следует удалить")
                            index = input()
                            date_time_base.delete_by_index(index)
                        elif key == "3":

                            """Администратор -> Контейнер -> Изменить объект в контейнере"""

                            print(f"Список созданных объектов Дата/Время:\n{date_time_base.__str__()}\n"
                                  "Введите индекс объекта, с которым хотите работать")
                            index = input()
                            date_time_object = date_time_base.__getitem__(index)
                            if date_time_object is None:
                                continue
                            print("День:")
                            date_time_object.day = input()
                            print("Месяц:")
                            date_time_object.month = input()
                            print("Год:")
                            date_time_object.year = input()
                            print("Час:")
                            date_time_object.hour = input()
                            print("Минута:")
                            date_time_object.minute = input()
                        elif key == "4":
                            
                            """Администратор -> Контейнер -> Сохранить в JSON"""

                            date_time_base.json_save()
                            print("Контейнер сохранен в локальную папку в файл date_time_container.json")
                        elif key == "5":

                            """Администратор -> Контейнер -> Загрузить из JSON"""

                            print("Введите относительный или абсолютный адрес сохранения файла")
                            filepath = input()
                            date_time_base.json_load(filepath)
                        elif key == "6":
                            break
                elif key == "3":
                    break
