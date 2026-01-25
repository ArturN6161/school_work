class Figure:
    def area(self):
        pass


    def perimetr(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Такого треугольника не существует!')


    def __str__(self):
        return f'Треугольник со сторонами a, b, c: {self.a}, {self.b}, {self.c} соответственно'


    def perimetr(self):
        return self.a + self.b + self.c


    def area(self):
        n = (self.a + self.b + self.c) / 2
        return (n * (n - self.a)*(n - self.b)*(n - self.c))**(1/2)


class Circle(Figure):
    def __init__(self, a):
        if a > 0:
            self.a = a
            self.number_pi = 3.1412
        else:
            print('Круга с радиусом 0 не существует. Этот объект является точкой!')


    def __str__(self):
        return f'Круг с радиусом {self.a}'


    def perimetr(self):
        return 2 * self.number_pi * self.a


    def area(self):
        return self.number_pi * self.a ** 2


class Rectangle(Figure):
    def __init__(self, a, b):
       if a != 0 and b != 0:
            self.a = a
            self.b = b
       else:
           print("Объект не является прямоугольником!")


    def __str__(self):
        return f'Прямоугольник со сторонами a, b: {self.a}, {self.b} соответственно'


    def area(self):
        return self.a * self.b


    def perimetr(self):
        return (self.a + self.b) * 2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Квадрат со сторонами a: {self.a}'


class Equilateral_triangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


    def __str__(self):
        return f'Эллипс с полуосями a, b: {self.a}'


class Ellips(Circle):
    def __init__(self, a, b):
        if a > 0 and b > 0:
            super().__init__(a)
            self.b = b


    def __str__(self):
        return f'Эллипс с полуосями a, b: {self.a}, {self.b}'


    def area(self):
        return self.a * self.b * self.number_pi


    def perimetr(self):
        return self.number_pi * (3*(self.a + self.b) - ((3 * self.a + self.b) * (self.a + 3 * self.b)) ** 0.5)

tri = Triangle(3, 4, 5)
cir = Circle(6)
rect = Rectangle(7, 8)
tri_eq = Equilateral_triangle(9)
sq = Square(10)
el = Ellips(11, 12)

figures = (tri, cir, rect, tri_eq, sq, el,)

for f in figures:
    print("="*35)
    print(f'Фигура: {f.__class__.__name__}')
    print(f)
    print(f'Периметр: {f.perimetr():.2f}')
    print(f'Площадь: {f.area():.2f}')