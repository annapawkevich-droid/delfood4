from patterns.notifier_observer import NotifierSubject, EmailNotifier, SmsNotifier

class NotificationService:
    def __init__(self):
        self.subject = NotifierSubject()

    def setup(self, email: str, phone: str):
        self.subject.subscribe(EmailNotifier(email))
        self.subject.subscribe(SmsNotifier(phone))

    def notify(self, message: str):
        self.subject.notify_all(message)
