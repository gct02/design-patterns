from abc import ABC, ABCMeta, abstractmethod

class Shape(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = side

    def clone(self):
        return Square(self.side)
    
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def clone(self):
        return Circle(self.radius)
    
if __name__ == "__main__":
    circle = Circle(2)
    circle_clone = circle.clone()

    print(f"Original circle radius is {circle.radius}, cloned circle is {circle_clone.radius}.")