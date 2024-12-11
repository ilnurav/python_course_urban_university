import math

class Figure:
    def __init__(self, color, *sides):
        self.sides_count = 0
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
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 1
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        sides = self.get_sides()
        if not sides:  # Проверка на пустой список сторон
            return 1  # Если сторон нет, радиус по умолчанию 1
        return sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12
        super().__init__(color, *sides)
        self.__sides = self.__validate_sides(sides)

    def __validate_sides(self, sides):
        if len(sides) == 1:
            return [sides[0]] * self.sides_count
        return [1] * self.sides_count

    def get_volume(self):
        sides = self.get_sides()
        if not sides:  # Проверка на пустой список сторон
            return 1  # Если сторон нет, объем по умолчанию 1
        return sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())