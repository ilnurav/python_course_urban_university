# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        # Попытка сложить a и b
        return a + b
    except TypeError:
        # Если возникла ошибка TypeError, возвращаем строковое представление a и b
        return f"{a}{b}"

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))    # Вывод: яблоко4215
print(add_everything_up(123.456, 7))        # Вывод: 130.456