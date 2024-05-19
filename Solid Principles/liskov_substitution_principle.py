# Before LSP
class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    pass


class Eagle(Bird):
    pass


class Penguin(Bird):  # This is not acceptable
    def fly(self):
        raise NotImplementedError("Penguins can't fly")


# After LSP
from abc import ABC, abstractmethod


class Bird:
    # General bird properties and methods
    pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(Bird, Flyable):
    def fly(self):
        print("Flying")


class Eagle(Bird, Flyable):
    def fly(self):
        print("Flying high")


class Penguin(Bird):
    # Penguins don't implement Flyable
    pass
