# Strategy Pattern in Python
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal.")


class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: float):
        self.strategy.pay(amount)


# Usage
cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)  # Output: Paying 100 using Credit Card.

cart.set_strategy(PayPalPayment())
cart.checkout(200)  # Output: Paying 200 using PayPal.


# Reconstructed Strategy Pattern in Python

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal.")


class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: float):
        self.strategy.pay(amount)


# Normal Abstraction in Python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Square(Shape):
    def draw(self):
        print("Drawing a square")
