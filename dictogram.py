class Dictogram(dict):
    """It's a dictionary."""

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items."""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable."""
        capitalize_these = ('i')
        for item in iterable:
            if item in capitalize_these:
                item = item.capitalize()
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
                self.types += 1
            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0."""
        return self.get(item, 0)
