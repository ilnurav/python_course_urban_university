# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):
    matrix = []
    if value > 0:
        for i in range(n):
            row = []
            for j in range(m):
                row.append(value)
            matrix.append(row)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1) # [[10, 10], [10, 10]]
print(result2) # [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(result3) # [[13, 13], [13, 13], [13, 13], [13, 13]]