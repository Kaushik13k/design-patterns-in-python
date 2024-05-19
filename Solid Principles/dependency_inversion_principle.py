from abc import ABC, abstractmethod


# Step 2: Create Abstractions
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Step 3: Implement Low-Level Modules
class PaypalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment through PayPal: {amount}")


class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment through Stripe: {amount}")


# Step 4: Implement High-Level Module
class PaymentService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def make_payment(self, amount):
        self.payment_gateway.process_payment(amount)


# Step 5: Use Dependency Injection to Decouple Dependencies
def main():
    paypal_gateway = PaypalGateway()
    payment_service = PaymentService(paypal_gateway)
    payment_service.make_payment(100.0)

    stripe_gateway = StripeGateway()
    payment_service = PaymentService(stripe_gateway)
    payment_service.make_payment(200.0)


if __name__ == "__main__":
    main()
