# Дополнительное практическое задание по модулю: "Наследование классов."

import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.filled = False
        self.__color = list(color)
        self.__sides = self.__validate_sides(sides)

    def __validate_sides(self, sides):
        if len(sides) == self.sides_count:
            if all(isinstance(side, int) and side > 0 for side in sides):
                return list(sides)
        return [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 for value in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == len(self.__sides)
                and all(isinstance(side, int)
                        and side > 0 for side in new_sides))

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == self.sides_count:
            self.__radius = sides[0]
        else:
            self.__radius = [1]

    def get_square(self):
        return math.pi * self.__radius[0] ** 2



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count

    def get_square(self):
        sides = self.get_sides()
        a, b, c = sides[0], sides[1], sides[2]
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color()) # [55, 66, 77]
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color()) # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides()) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15) # Изменится
print(circle1.get_sides()) # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1)) # 15

# Проверка объёма (куба):
print(cube1.get_volume()) # 216
