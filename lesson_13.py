# Домашняя работа по уроку "Пространство имён"

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [s.lower() for s in list_to_search]
    return string.lower() in list_to_search

print(string_info('Capybara')) # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon')) # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # True
print(is_contains('cycle', ['recycling', 'cyclic'])) # False
print(calls)