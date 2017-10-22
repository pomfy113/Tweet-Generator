class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.tokens += 1
            if not self.__contains__(item):
                self.append((item, 1))
                self.types += 1
            else:
                for word, value in self:
                    if item == word:
                        self[self._index(item)] = (word, value+1)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if not self.__contains__(item):
            return 0
        else:
            for word, value in self:
                if word == item:
                    return value

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False."""
        return any(item in word for word in self)

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None."""
        if self.__contains__(target) is False:
            return None
        else:
            for index, word in enumerate(self):
                if target in word:
                    return index
