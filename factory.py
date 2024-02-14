from abc import ABC, ABCMeta, abstractmethod
from math import pi

# Abstract product
class Shape(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        return

# Concrete product 1
class Square(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = side

    def calculate_area(self):
        return self.side ** 2

# Concrete product 2
class Rectangle(Shape):
    def __init__(self, base, height):
        self._base = base
        self._height = height

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        self._base = base

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height

    def calculate_area(self):
        return self.base * self.height

# Concrete product 3
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * pi * self.radius

# Abstract factory
class ShapeFactory(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_shape(self) -> Shape:
        return

# Concrete factory 1
class SquareFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Square(None)

# Concrete factory 2
class RectangleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Rectangle(None, None)

# Concrete factory 3
class CircleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Circle(None)
    
if __name__ == "__main__":
    factory = SquareFactory()
    shape = factory.create_shape()
    shape.side = 2
    print(shape.calculate_area())

    factory = CircleFactory()
    shape = factory.create_shape()
    shape.radius = 2
    print(shape.calculate_area())

    factory = RectangleFactory()
    shape = factory.create_shape()
    shape.base = 2
    shape.height = 4
    print(shape.calculate_area())