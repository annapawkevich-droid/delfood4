from typing import List
from models.dish import Dish
from models.customer import Customer

class Order:
    def __init__(self, order_number: int, customer: Customer):
        self.order_number = order_number
        self.customer = customer
        self.items: List[Dish] = []
        self.discount_percent = 0
        self.total = 0.0
        self.status = "CREATED"

    def add_item(self, dish: Dish):
        self.items.append(dish)

    def calc_subtotal(self) -> float:
        return sum(d.price for d in self.items)

    def calc_total(self):
        subtotal = self.calc_subtotal()
        self.total = subtotal * (1 - self.discount_percent / 100)
        return self.total

    def __str__(self): #вивіл у вигляді ріядка
        items_text = "\n".join([f"- {d.name} ({d.price:.2f} грн)" for d in self.items]) if self.items else "— немає"
        return (
            f"\nЗамовлення №{self.order_number}\n"
            f"Клієнт: {self.customer.name}\n"
            f"Страви:\n{items_text}\n"
            f"Знижка: {self.discount_percent}%\n"
            f"Сума: {self.total:.2f} грн\n"
            f"Статус: {self.status}"
        )
