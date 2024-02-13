from abc import ABC, ABCMeta, abstractmethod

# Abstract Car
class Car(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_engine_type(self):
        pass

# Concrete Car 1
class ElectricCar(Car):
    def __init__(self):
        pass

    def get_engine_type(self):
        print("Electric car engine")

# Concrete Car 2
class CombustionCar(Car):
    def __init__(self):
        pass

    def get_engine_type(self):
        print("Combustion car engine")

# Abstract Bike
class Bike(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_engine_type(self):
        pass

# Concrete Bike 1
class ElectricBike(Bike):
    def __init__(self):
        pass

    def get_engine_type(self):
        print("Electric bike engine")

# Concrete Bike 2
class CombustionBike(Bike):
    def __init__(self):
        pass

    def get_engine_type(self):
        print("Combustion bike engine")

# Abstract factory
class VehicleFactory(ABC):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_bike(self):
        pass

# Concrete factory 1
class ElectricVehicleFactory(VehicleFactory):
    def __init__(self):
        pass

    def create_car(self):
        return ElectricCar()
    
    def create_bike(self):
        return ElectricBike()

# Concrete factory 2
class CombustionVehicleFactory(VehicleFactory):
    def __init__(self):
        pass

    def create_car(self):
        return CombustionCar()
    
    def create_bike(self):
        return CombustionBike()
    
if __name__ == "__main__":
    factory = ElectricVehicleFactory()

    car = factory.create_car()
    car.get_engine_type()

    bike = factory.create_bike()
    bike.get_engine_type()

    factory = CombustionVehicleFactory()

    car = factory.create_car()
    car.get_engine_type()

    bike = factory.create_bike()
    bike.get_engine_type()