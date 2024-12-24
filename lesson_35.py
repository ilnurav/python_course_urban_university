# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return f"{a}{b}"

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456
