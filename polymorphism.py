# Polymorphism
print(10 + 256)
print("Python" + "programming")

# Function of Polymorphism
print(len(["Python", "PHP", "C++"]))
print(len({"Name": "kaushik", "Address": "Bangalore,India"}))


# Class example for Polymorphism
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Cow. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Moo")


cat1 = Cat("Kitty", 2.5)
cow1 = Cow("Fluffy", 4)

for animal in (cat1, cow1,):  # polymorphism as we are calling same method name and getting different output for cow and cat
    animal.make_sound()
    animal.info()
    animal.make_sound()


# Method overriding
class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

    def fetch(self):
        print("Dog fetches")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

    def scratch(self):
        print("Cat scratches")


# Example of overriding
dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()


# Example of overloading (Python does not support method overloading directly, but it can be simulated)
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


# Only the latest definition of the method 'add' is considered
calculator = Calculator()
print(calculator.add(2, 3))  # This wont work
print(calculator.add(2, 3, 4))  # This will work
