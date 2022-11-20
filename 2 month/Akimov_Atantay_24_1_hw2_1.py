class Figure:
    unit = 'cm'
    def __init__(self, perimeter=0 ):
        self.__perimeter = perimeter

    def calculate_perimeter(self):
        perimetr = self.side_length * 4
        return perimetr
        self.__perimeter == perimetr

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def info(self):
        pass

class Sguare(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_perimeter(self):
        perimetr = self.__side_length * 4
        return perimetr

    def calculate_area(self):
        area = self.__side_length * 2
        return area

    def info(self):
        perimetr = self.__side_length * 4
        area = self.__side_length * 2
        print(f' Square side length: {self.__side_length}{self.unit}, perimeter: {perimetr}{self.unit}, area: {area}{self.unit}')

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width


sguare = Sguare(2)
sguare.info()
sguare.calculate_perimeter()




