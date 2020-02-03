# Single Responsibility principle
# Every piece of code must do one, and only one, thing.


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


content_filter = ContentFilter([AdsFilter, OffensiveFilter])
filtered_result = content_filter.filter(['filter', 'me', 'bad', 'guy', 'and', 'buy', 'x'])
print(filtered_result)
