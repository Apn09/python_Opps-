from abc import ABC, abstractmethod

# Abstraction
class DeliveryService(ABC):

    def __init__(self, customer):
        self.customer = customer

    @abstractmethod
    def deliver(self):
        pass


# Inheritance
class BikeDelivery(DeliveryService):

    def deliver(self):
        print(f"Order delivered to {self.customer} using Bike")


class CarDelivery(DeliveryService):

    def deliver(self):
        print(f"Order delivered to {self.customer} using Car")


# Encapsulation
class Wallet:

    def __init__(self, balance):
        self.__balance = balance   # private variable

    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Payment successful:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Remaining balance:", self.__balance)


# Polymorphism
class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


# Main Program

# Encapsulation example
wallet = Wallet(2000)
wallet.pay(500)
wallet.show_balance()

print("paid 1500 using wallet")

# Polymorphism example
payment1 = UPI()
payment2 = CreditCard()

payment1.pay(300)
payment2.pay(700)

print("paid 300 using UPI and 700 using Credit Card")

# Inheritance + Abstraction example
delivery1 = BikeDelivery("Anand")
delivery2 = CarDelivery("Rahul")

delivery1.deliver()
delivery2.deliver()
