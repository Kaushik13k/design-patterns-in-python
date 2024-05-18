# Before OCP
class PaymentProcessor:
    def process_credit_card_payment(self, amount):
        # logic to process credit card payment
        pass


class PaymentProcessor:
    def process_credit_card_payment(self, amount):
        # logic to process credit card payment
        pass

    def process_paypal_payment(self, amount):
        # logic to process PayPal payment
        pass


# After OCP
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        # logic to process credit card payment
        pass


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        # logic to process PayPal payment
        pass


class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        payment_method.process_payment(amount)
