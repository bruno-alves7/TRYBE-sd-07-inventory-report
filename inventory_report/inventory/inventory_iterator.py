from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list):
        self.list = list
        self.index = -1

    def __next__(self):
        try:
            self.index += 1
            return self.list[self.index]
        except IndexError:
            raise StopIteration()
