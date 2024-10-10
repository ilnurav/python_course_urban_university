# Дополнительное практическое задание по модулю 2 "Основные операторы"

def passw(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

print(passw(int(input('Введите n: '))))