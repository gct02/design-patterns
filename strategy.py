from abc import ABC, ABCMeta, abstractmethod
from enum import Enum

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AdditionStrategy(Strategy):
    def execute(self, a, b):
        return a + b
    
class SubtractionStrategy(Strategy):
    def execute(self, a, b):
        return a - b
    
class MultiplicationStrategy(Strategy):
    def execute(self, a, b):
        return a * b
    
class Context:
    def __init__(self, strategy : Strategy = None):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)
    
if __name__ == "__main__":
    context = Context()

    action = int(input("1: Addition\n2: Subtraction\n3: Multiplication\nEnter desired action: "))

    match action:
        case 1:
            context.strategy = AdditionStrategy()
        case 2:
            context.strategy = SubtractionStrategy()
        case 3:
            context.strategy = MultiplicationStrategy()
        case _:
            context.strategy = None
            print("Invalid strategy")
    
    if (context.strategy is not None):
        a = int(input("a: "))
        b = int(input("b: "))
        result = context.execute_strategy(a, b)
        print(f"Result: {result}")
