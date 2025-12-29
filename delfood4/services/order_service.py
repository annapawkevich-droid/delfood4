from models.order import Order
from patterns.discount_strategy import DiscountStrategy

class OrderService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        self._counter = 1

    def create_order(self, customer):
        order = Order(self._counter, customer)
        self._counter += 1
        return order

    def apply_discount(self, order: Order, promo_code: str):
        subtotal = order.calc_subtotal()
        order.discount_percent = self.discount_strategy.get_discount_percent(promo_code, subtotal)
        order.calc_total()
        return order.discount_percent
