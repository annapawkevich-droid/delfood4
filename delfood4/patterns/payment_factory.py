import random

class PaymentMethod:
    def pay(self, amount: float) -> bool:
        return False

class CardPayment(PaymentMethod):
    def __init__(self, card_number: str, exp: str, cvv: str):
        self.card_number = card_number
        self.exp = exp
        self.cvv = cvv

    def pay(self, amount: float) -> bool:
        return random.choice([True, False])

class ApplePayPayment(PaymentMethod):
    def __init__(self, device_confirm: str):
        self.device_confirm = device_confirm

    def pay(self, amount: float) -> bool:
        return random.choice([True, False])

class PaymentFactory:#створює потрібний спосіб оплати в одному місці, щоб не писати купу if у main
    @staticmethod
    def create(method_choice: int, payload: dict) -> PaymentMethod:
        if method_choice == 1:
            return CardPayment(payload["card_number"], payload["exp"], payload["cvv"])
        elif method_choice == 2:
            return ApplePayPayment(payload["confirm"])
        else:
            raise ValueError("Невірний спосіб оплати")
