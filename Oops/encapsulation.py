# public members & public access modifier
class PublicClass:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        # accessing public data member
        print(f"The age is: {self.age}")


# creating object
obj_public = PublicClass("kaushik", 10)

# accessing public data member
obj_public.name

# calling public member function of the class
obj_public.print_age()


# private members & private access modifier
# double underscore __ => private
class PrivateClass:
    def __init__(self, dob, address):
        self.__dob = dob  # private
        self.__address = address  # private

    def get_dob(self):  # Getter method to access the private variable
        print(f"DOB is: {self.__dob}")

    def get_address(self):
        print(f"address is: {self.__address}")

    def set_dob(self, dob):  # Setter method to modify the private variable
        self.__dob = dob
        print(f"DOB after setting is: {self.__dob}")

    def set_address(self, address):
        self.__address = address
        print(f"address after setting is: {self.__address}")


# creating object
obj_private = PrivateClass(20240516, "hello world")

#  Accessing private members directly won't work
# obj_private.__dob  # Wont work as it is set private
# obj_private.__dob  # Wont work as it is set private

# Accessing private members through getter methods
obj_private.get_dob()  # to access the data
obj_private.get_address()  # to access the data

# Modifying private members through setter methods
obj_private.set_dob(20240517)  # to edit the data
obj_private.set_address("hello world2")  # to edit the data
