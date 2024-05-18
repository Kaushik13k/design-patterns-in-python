# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")


# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says woof!"


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says meow!"


# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())
# print(cat.speak())


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
