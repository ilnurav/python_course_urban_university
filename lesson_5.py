# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = (10, 5.9, 'hello', True)
print('Immutable tuple:', immutable_var)
immutable_var[0] = 20 # выйдет ошибка, т.к. кортеж - неизменяемый объект
mutable_list = [10, 5.9, 'hello', True]
mutable_list[0] = 20
mutable_list[1] = 4.7
mutable_list[2] = 'world'
mutable_list[3] = False
print('Mutable list:', mutable_list)




