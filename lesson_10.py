# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number > 1:
        for j in range(2, round(number ** 0.5) + 1):
            if number % j == 0:
                not_primes.append(number)
                break
        else:
            primes.append(number)
print(f'Primes: {primes}') # [2, 3, 5, 7, 11, 13]
print(f'Not Primes: {not_primes}') # [4, 6, 8, 9, 10, 12, 14, 15]