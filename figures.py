class Figure:
    def square(self):
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


    def square(self):
        n = (self.a + self.b + self.c) / 2
        return (n * (n - self.a)*(n - self.b)*(n - self.c))**(1/2)


class Circle(Figure):
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
            self.number_pi = 3.1412
        else:
            print('Круга с радиусом 0 не существует. Этот объект является точкой!')


    def __str__(self):
        return f'Круг с радиусом {self.radius}'


    def perimetr(self):
        return 2 * self.number_pi * self.radius


    def square(self):
        return self.number_pi * self.radius ** 2


class Rectangle(Figure):
    def __init__(self, a, b):
       if a != 0 and b != 0:
            self.a = a
            self.b = b
       else:
           print("Объект не является прямоугольником!")


    def __str__(self):
        return f'Прямоугольник со сторонами a, b: {self.a}, {self.b} соответственно'


    def square(self):
        return self.a * self.b


    def perimetr(self):
        return (self.a + self.b) * 2


tri = Triangle(3, 4, 5)
cir = Circle(6)
rect = Rectangle(7, 8)

figures = [tri, cir, rect]

for f in figures:
    print("="*35)
    print(f'Фигура: {f.__class__.__name__}')
    print(f)
    print(f'Периметр: {f.perimetr():.2f}')
    print(f'Площадь: {f.square():.2f}')