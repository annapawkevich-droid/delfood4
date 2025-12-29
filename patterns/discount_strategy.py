class DiscountStrategy:#відповідає за знижку — можна змінювати правила знижок без переписування класу замовлення
    def get_discount_percent(self, promo_code: str, subtotal: float) -> int:
        return 0

class NoDiscountStrategy(DiscountStrategy):
    def get_discount_percent(self, promo_code: str, subtotal: float) -> int:
        return 0

class PromoDiscountStrategy(DiscountStrategy):
    PROMOS = {
        "SAVE10": 10,
        "SAVE20": 20,
    }

    def get_discount_percent(self, promo_code: str, subtotal: float) -> int:
        promo_code = (promo_code or "").strip().upper()
        return self.PROMOS.get(promo_code, 0)
