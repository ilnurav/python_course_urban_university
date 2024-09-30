# Практическое задание по теме: "Словари и множества"

my_dict = {'Петя': 1997, 'Юля': 2000, 'Костя': 2001}
print('Dict', my_dict)
print('Existing value:', my_dict['Юля'])
print('Not existing value:', my_dict.get('Оля', None))
my_dict['Толя'] = 1998
my_dict['Юра'] = 1993
print('Deleted value:', my_dict.pop('Юля'))
print('Modified dictionary:', my_dict)

my_set = {3, 3, 'hello', 3, 'hello', 3.9, 3.9}
print('Set:', my_set)
my_set.add(True)
my_set.add((9, 7.4, 10))
my_set.remove(3)
print('Modified set:', my_set)
