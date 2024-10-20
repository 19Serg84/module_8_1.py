def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # Если оба аргумента числа (int или float), складываем их
            return a + b
        else:
            # Если типы различаются (число и строка), выбросим исключение
            raise TypeError
    except TypeError:
        # Обрабатываем исключение и возвращаем строковое представление значений
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))      # Вывод: яблоко4215
print(add_everything_up(123.456, 7))           # Вывод: 130.456