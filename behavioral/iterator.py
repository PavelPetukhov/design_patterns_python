from collections.abc import Iterable, Iterator

# Provide a way to access the elements of an aggregated object sequentially
# without exposing its underlying representation
# The key idea in this pattern is to take the responsibility for access and
# traversal out of the list object and put it into an iterator object


class CustomCollection:
    def __init__(self, collection_):
        self._collection = collection_

    def __iter__(self):
        return CustomIterator(self._collection)


class CustomIterator(Iterator):
    def __init__(self, collection_: CustomCollection):
        self._collection = collection_
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value
