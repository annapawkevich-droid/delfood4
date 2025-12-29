from patterns.payment_factory import PaymentFactory

class PaymentService:
    def process_payment(self, order, method_choice: int, payload: dict) -> bool:
        payment_method = PaymentFactory.create(method_choice, payload)
        return payment_method.pay(order.total)
