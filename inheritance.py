# # syntax:
# class DerivedClass(BaseClass):
#     pass


class Person:  # BaseClass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello my name is {self.name}, my age is {self.age}")


class Student(Person):  # Student Inheriting the person class
    def __init__(self, name, age, grade):
        super().__init__(
            name, age
        )  # Call the parent class constructor to initialize name and age
        self.grade = grade

    def say_grade(self):
        # super().say_hello()  # Call the parent class say_hello method to introduce the student as a person
        print(f"And my grade is: {self.grade}")


# Creating an instance of the base class
person = Person("John", 30)
person.say_hello()

# Creating an instance of the derived class
student = Student("Mary", 18, 12)
student.say_hello()
student.say_grade()


# Types of inheritance
# 1. Single Inheritance


class Parent:  # parent class
    def func1(self):
        print("parent func1")


class Child(Parent):  # child class
    def func2(self):
        print("child func2")


obj = Child()
obj.func1()  # parent method called via child object
obj.func2()


# 2. Multiple Inheritance
class Parent1:  # first parent class
    def func1(self):
        print("parent func1")


class Parent2:  # second parent class
    def func2(self):
        print("parent func2")


class Parent3:  # third parent class
    def func3(self):
        print("parent func3")


class Child(Parent1, Parent2, Parent3):  # child class
    def func4(self):
        print("child func4")


obj1 = Child()
obj1.func1()  # parent1 method called via child
obj1.func2()  # parent2 method called via child instead of parent3
obj1.func4()

# In Python, __mro__ stands for Method Resolution Order.
# It's an attribute of a class that shows the order in which base classes are searched when executing a method.
# This order is important in the context of multiple inheritance, where a class can inherit from more than one parent class.
print(Child.__mro__)


# 3. Multilevel Inheritance
class grandparent:  # first level
    def func1(self):
        print("Hello Grandparent")


class parent(grandparent):  # second level
    def func2(self):
        print("Hello Parent")


class child(parent):  # third level
    def func3(self):
        print("Hello Child")


# Driver Code
test = child()  # object created
test.func1()  # 3rd level calls 1st level
test.func2()  # 3rd level calls 2nd level
test.func3()  # 3rd level calls 3rd level

print(Child.__mro__)


# 4. Hierarchical Inheritance
# python 3 syntax
# hierarchical inheritance example


class parent:  # parent class
    def func1(self):
        print("Hello Parent")


class child1(parent):  # first child class
    def func2(self):
        print("Hello Child1")


class child2(parent):  # second child class
    def func3(self):
        print("Hello Child2")


# Driver Code
test1 = child1()  # objects created
test2 = child2()

test1.func1()  # child1 calling parent method
test1.func2()  # child1 calling its own method

test2.func1()  # child2 calling parent method
test2.func3()  # child2 calling its own method


# Method Overriding
# Ex 1:
class parent:  # parent class

    def __init__(self):  # __init__() of parent
        self.attr1 = 50
        self.attr2 = 66


class child(parent):  # child class

    def __init__(self):  # __init__() of child
        parent.__init__(self)  # calling parent’s __init__()
        self.attr3 = 45


test = child()  # object initiated

print(test.attr1)  # parent attribute called via child


#  Ex 2:
class parent:  # parent class

    def display(self):  # display() of parent
        print("Hello Parent")


class child(parent):  # child class

    def display(self):  # display() of child
        super().display()  # referencing parent via super()
        print("Hello Child")


test = child()  # object initiated

test.display()  # display of both activated


# issubclass(), isinstance()
class parent:  # parent class
    def func1():
        print("Hello Parent")


class child(parent):  # child class
    def func2():
        print("Hello Child")


# Driver Code

print(issubclass(child, parent))  # checks if child is subclass of parent

print(issubclass(parent, child))  # checks if parent is subclass of child

A = child()  # objects initialized
B = parent()

print(isinstance(A, child))  # checks if A is instance of child
print(isinstance(A, parent))  # checks if A is instance of parent
print(isinstance(B, child))  # checks if B is instance of child
print(isinstance(B, parent))  # checks if B is instance of parent
