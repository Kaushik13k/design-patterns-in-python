from abc import ABC, abstractmethod


# Define specific interfaces using ABCs
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Chirpable(ABC):
    @abstractmethod
    def chirp(self):
        pass


# Implementing specific interfaces in bird classes
class Sparrow(Flyable, Chirpable):
    def fly(self):
        print("Sparrow is flying")

    def chirp(self):
        print("Sparrow is chirping")


class Penguin(Swimmable, Chirpable):
    def swim(self):
        print("Penguin is swimming")

    def chirp(self):
        print("Penguin is chirping")


# Using the classes
def main():
    sparrow = Sparrow()
    penguin = Penguin()

    sparrow.fly()
    sparrow.chirp()

    penguin.swim()
    penguin.chirp()


if __name__ == "__main__":
    main()
