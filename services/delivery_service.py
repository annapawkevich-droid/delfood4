import random

class DeliveryService:
    def assign_delivery(self, order):
        courier = random.choice(["Іван", "Олег", "Марина", "Таня"])
        minutes = random.randint(20, 60)
        return courier, minutes
