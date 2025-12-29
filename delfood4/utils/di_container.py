from patterns.discount_strategy import PromoDiscountStrategy
from services.menu_service import MenuService
from services.order_service import OrderService
from services.payment_service import PaymentService
from services.delivery_service import DeliveryService
from services.notification_service import NotificationService
from services.repository import OrderRepository

class DIContainer:
    def __init__(self):
        # Strategy
        discount_strategy = PromoDiscountStrategy()

        # Services
        self.menu_service = MenuService()
        self.order_service = OrderService(discount_strategy)
        self.payment_service = PaymentService()
        self.delivery_service = DeliveryService()
        self.notification_service = NotificationService()
        self.repository = OrderRepository()
