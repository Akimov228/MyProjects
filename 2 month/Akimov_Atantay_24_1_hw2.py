class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        r = self.__radius**2 * 3.14
        return  r


    def info(self):
        r = (self.__radius**2 * 3.14)

        print(f'Circle radius: {self.__radius}{self.unit}, area: {r}{self.unit}.')

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        area = self.__side_a * self.__side_b / 2
        return area

    def info(self):
        s = self.__side_a * self.__side_b / 2
        print(f'RightTriangle side a: {self.__side_a}{self.unit} side b: {self.__side_b}{self.unit} area: {s}{self.unit}')


circle1 = Circle(2)
circle2 = Circle(3)

triangle1 = RightTriangle(2, 3)
triangle2 = RightTriangle(4, 3)
triangle3 = RightTriangle(5, 3)

figures = [circle1,circle2,triangle1,triangle2,triangle3]

for i in figures:
    i.info()



