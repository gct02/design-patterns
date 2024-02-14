from abc import ABC, ABCMeta, abstractmethod
from enum import Enum

class Engine:
    def __init__(self, volume, mileage):
        self._volume = volume
        self._mileage = mileage

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, volume):
        self._volume = volume

    @property
    def mileage(self):
        return self._mileage
    
    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage

    def __str__(self):
        return f"Volume: {self._volume}, Mileage: {self._mileage}"

class Transmission(Enum):
    SINGLE_SPEED = 1
    MANUAL = 2
    AUTOMATIC = 3
    SEMI_AUTOMATIC = 4

    

class Car:
    def __init__(self, doors, seats, engine, transmission):
        self._doors = doors
        self._seats = seats
        self._engine = engine
        self._transmission = transmission

    @property
    def doors(self):
        return self._doors
    
    @doors.setter
    def doors(self, doors):
        self._doors = doors

    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self, seats):
        self._seats = seats

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def transmission(self):
        return self._transmission
    
    @transmission.setter
    def transmission(self, transmission):
        self._transmission = transmission

    def __str__(self):
        return f"Doors: {self._doors}, Seats: {self._seats}, " + str(self._engine) + ", Transmission: " + self._transmission.name

class Builder(ABC):
    @abstractmethod
    def set_doors(self, doors : int):
        pass

    @abstractmethod
    def set_seats(self, seats : int):
        pass

    @abstractmethod
    def set_engine(self, engine : Engine):
        pass

    @abstractmethod
    def set_transmission(self, transmission : Transmission):
        pass

class CarBuilder(Builder):
    def set_doors(self, doors : int):
        self.__doors = doors

    def set_seats(self, seats: int):
        self.__seats = seats

    def set_engine(self, engine: Engine):
        self.__engine = engine 

    def set_transmission(self, transmission: Transmission):
        self.__transmission = transmission

    def get_result(self) -> Car:
        return Car(self.__doors, self.__seats, self.__engine, self.__transmission)
    
if __name__ == "__main__":
    engine = Engine(1.6, 10000)
    transmission = Transmission.AUTOMATIC

    car_builder = CarBuilder()

    car_builder.set_doors(4)
    car_builder.set_seats(5)
    car_builder.set_engine(engine)
    car_builder.set_transmission(transmission)

    car = car_builder.get_result()

    print(str(car))
