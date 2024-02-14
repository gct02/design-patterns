from abc import ABC, ABCMeta, abstractmethod
from typing import List

class Observer:
    pass

class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber : Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, subscriber : Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcretePublisher(Publisher):
    _state : int = 0
    _subscribers : List[Observer] = []

    @property
    def state(self) -> int:
        return self._state
    
    def subscribe(self, subscriber : Observer) -> None:
        print("Publisher: Subscription added.")
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Observer) -> None:
        self._subscribers.remove(subscriber)

    def notify(self) -> None:
        print("Publisher: Notifying subscribers...")
        for subscriber in self._subscribers:
            subscriber.update(self)

    def business_logic(self) -> None:
        # Publisher's business logic can trigger a notification 
        # whenever something important happens
        self._state += 1

        print(f"Publisher: State changed to {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, publisher : Publisher) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, publisher: Publisher) -> None:
        if publisher.state % 2 == 0:
            print("ConcreteObserverA: Reacted to the event when state is even.")

class ConcreteObserverB(Observer):
    def update(self, publisher: Publisher) -> None:
        if publisher.state % 2 == 1:
            print("ConcreteObserverB: Reacted to the event when state is odd.")

if __name__ == "__main__":
    publisher = ConcretePublisher()
    
    observer_a = ConcreteObserverA()
    publisher.subscribe(observer_a)

    observer_b = ConcreteObserverB()
    publisher.subscribe(observer_b)

    publisher.business_logic()
    publisher.business_logic()
    publisher.business_logic()
    publisher.business_logic()

    publisher.unsubscribe(observer_a)
    publisher.business_logic()

