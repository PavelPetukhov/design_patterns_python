
# Chain of Responsibility is a behavioral design pattern
# that lets you pass requests along a chain of handlers.
# Upon receiving a request, each handler decides either
# to process the request or to pass it to the next handler in the chain.

# Example 1: Filtering msgs
# Single Responsibility principle
# Every piece of code must do one, and only one, thing.


# Example 2 with connected handlers
# checking if number is valid


import abc

#
#     EXAMPLE 1
#


class ContentFilter:
    def __init__(self, filters=None):
        self._filters = list()
        if filters:
            self._filters += filters

    def filter(self, content):
        for filter_ in self._filters:
            content = filter_.filter(content)
        return content


class AdsFilter:
    @staticmethod
    def filter(content):
        return [item for item in content if item != 'buy']


class OffensiveFilter:
    @staticmethod
    def filter(content):
        return [item for item in content if item != 'bad']


#
#     EXAMPLE 2
#


class Handler(metaclass=abc.ABC):
    def __init__(self, next_handler_=None):
        self.next_handler = next_handler_

    def handle(self):
        pass

    @abc.abstractmethod
    def process(request):
        pass


class RangeHandler(Handler):

    @staticmethod
    def process(request):
        print(f'RangeHandler processing {request}')
        return 0 < request < 10


class EvenHandler(Handler):

    @staticmethod
    def process(request):
        return request % 2 == 0
