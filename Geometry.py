from math import pi

"""
Классы фигур
"""


# Фигура - начальный класс
class Shape:
    title = 'Figure'

    def area(self):
        pass

    def perimeter(self):
        pass

    @classmethod
    def figure_name(cls):
        return cls.title


# Квадрат
class Square(Shape):
    title = 'Square'

    def __init__(self, x: float):
        super().__init__()
        self.x = x

    def area(self):
        return self.x ** 2

    def perimeter(self):
        return self.x * 4


# Прямоугольник
class Rectangle(Square):
    title = 'Rectangle'

    def __init__(self, x: float, y: float):
        super().__init__(x)
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return (self.x + self.y) * 2


# Трапеция
class Trapezoid(Rectangle):
    title = 'Trapezoid'

    def __init__(self, x: float, y: float, h: float):
        super().__init__(x, y)
        self.h = h

    def area(self):
        return 0.5 * (self.x + self.y) * self.h

    def perimeter(self):
        return None


# Ромб
class Rhombus(Rectangle):
    title = 'Rhombus'

    def area(self):
        return super().area()

    def perimeter(self):
        return self.x * 4


# Треугольник
class Triangle(Rectangle):
    title = 'Triangle'

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z

    def area(self):
        return (self.geron() * (self.geron() - self.x) * (self.geron() - self.y) * (self.geron() - self.z)) ** 0.5

    def geron(self):
        return self.perimeter() / 2

    def perimeter(self):
        return self.x + self.y + self.y


# Круг
class Circle(Shape):
    title = 'Circle'

    def __init__(self, r: float):
        super().__init__()
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return self.r * pi * 2


"""
Классы трехмерных фигур получают новое свойство - объем
"""


# Куб
class Cube(Square):
    title = 'Cube'

    def area(self):
        return super().area() * 6

    def perimeter(self):
        return self.x * 12


# Паралепипед
class Parallelepiped(Trapezoid):
    title = 'Parallelepiped'

    def __init__(self, x: float, y: float, h: float):
        super().__init__(x, y, h)

    def area(self):
        return 2 * (self.x + self.y) * self.h

    def perimeter(self):
        return self.x * 4 + self.y * 4 + self.h * 4

    def volume(self):
        return self.x * self.y * self.h


# Сфера
class Sphere(Circle):
    title = 'Sphere'

    def __init__(self, r: float):
        super().__init__(r)

    def area(self):
        return super().area() * 4

    def volume(self):
        return 4 / 3 * pi * self.r ** 3


"""
Цилиндр, Конус , Треугольная пирамида 
имеют  дополнительно следующие свойства:
1. "Площадь основания"  
2. "Площадь боковой поверхности"

Из-за сложностей вычисления площади боковой поверхности и площади поверхности у треугольной пирамиды
реализация функций остутсвует
"""


# Цилиндр
class Cylinder(Circle):
    title = 'Cylinder'

    def __init__(self, r: float, h: float):
        super().__init__(r)
        self.h = h

    def area_base(self):
        return super().area()

    def side_area(self):
        return 2 * pi * self.r * self.h

    def area(self):
        return 2 * pi * self.r * (self.h + self.r)

    def volume(self):
        return pi * self.h * self.r ** 2


# Конус
class Cone(Cylinder):
    title = 'Cone'

    def __init__(self, r: float, h: float):
        super().__init__(r, h)

    def area_base(self):
        return super().area_base()

    def side_area(self):
        return pi * self.r * (self.h ** 2 + self.r ** 2) ** 0.5

    def area(self):
        return pi * self.r * (self.r + (self.r ** 2 + self.h ** 2) ** 0.5)

    def volume(self):
        return 1 / 3 * pi * self.h * self.r ** 2


# Треугольная пирамида
class TriangularPyramid(Triangle):
    title = 'Triangular pyramid'

    def __init__(self, x: float, y: float, z: float, h: float):
        super().__init__(x, y, z)
        self.h = h

    def area_base(self):
        return super().area()

    def side_area(self):
        pass

    def area(self):
        pass

    def volume(self):
        return 1 / 3 * self.area_base() * self.h
