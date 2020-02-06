import abc
from typing import List


class AbstractStrategy(metaclass=abc.ABCMeta):
    def do_algorithm(self, data: List):
        pass


class Context:
    def __init__(self, strategy: AbstractStrategy) -> None:
        self._strategy = strategy

    def business_logic(self, data):
        self._strategy.do_algorithm(data)

    @property
    def strategy(self) -> AbstractStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: AbstractStrategy):
        self._strategy = strategy


class ParticularStrategy1(AbstractStrategy):
    def do_algorithm(self, data: List):
        return sorted(data)


class ParticularStrategy2(AbstractStrategy):
    def do_algorithm(self, data: List):
        return reversed(data)



