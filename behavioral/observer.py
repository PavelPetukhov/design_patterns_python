import abc

from typing import List


class Observer(metaclass=abc.ABCMeta): pass


class Subject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abc.abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abc.abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def do_something_and_notify(self):
        self._state = 1
        self.notify()


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, subject: Subject):
        pass


class FirstConcreteObserver(Observer):

    def update(self, subject: Subject):
        pass


class SecondConcreteObserver(Observer):

    def update(self, subject: Subject):
        pass

