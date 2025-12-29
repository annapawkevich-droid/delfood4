class Observer:#після оплати статусу замовлення автоматично надсилає повідомлення клієнту, і можна легко додати новий тип повідомлення
    def update(self, message: str):
        pass

class EmailNotifier(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str):
        print(f"📧 Email на {self.email}: {message}")

class SmsNotifier(Observer):
    def __init__(self, phone: str):
        self.phone = phone

    def update(self, message: str):
        print(f"📱 SMS на {self.phone}: {message}")

class NotifierSubject:
    def __init__(self):
        self._observers = []

    def subscribe(self, obs: Observer):
        self._observers.append(obs)

    def notify_all(self, message: str):
        for obs in self._observers:
            obs.update(message)
