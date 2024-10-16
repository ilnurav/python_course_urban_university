# Домашнее задание по уроку "Распаковка позиционных параметров"

# 1. Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(10, 'hello', False) # 10 hello False
print_params(10, 'hello') # 10 hello True
print_params(10) # 10 строка True
print_params(a=10, b='hello', c=False) #
print_params(a=10, b='hello') # 10 hello False
print_params(c=10) # 10 hello True
print_params(b=25) # 1 строка 10
print_params(c=[1,2,3]) # 1 25 True

# 2. Распаковка параметров

values_list = [3, 'hello', True] # 3 hello True
values_dict = {'a': 5, 'b': 'world', 'c': True}
print_params(*values_list) # 3 hello True
print_params(**values_dict) # 5 world True

# 3. Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) # 54.32 Строка 42