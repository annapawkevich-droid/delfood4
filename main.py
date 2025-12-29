from utils.di_container import DIContainer
from utils.validators import (
    validate_name, validate_phone, validate_email, validate_int,
    validate_card_number, validate_exp, validate_cvv
)

def main():
    print("Food Delivery")

    di = DIContainer()

    #клієнт
    name = validate_name("Ваше ім'я: ")
    phone = validate_phone()
    email = validate_email()

    from models.customer import Customer
    customer = Customer(name, phone, email)

    #створюємо замовлення
    order = di.order_service.create_order(customer)

    #вибір страв
    while True: #нескінченний цикл 
        di.menu_service.show_menu()
        choice = validate_int("Оберіть страву (1-6) або 0 для завершення: ", 0, 6)
        if choice == 0:
            break
        dish = di.menu_service.get_dish_by_index(choice)
        order.add_item(dish)
        print(f"✅ Додано: {dish.name}")

    if not order.items:
        print("❌ Ви нічого не обрали. Завершення.")
        return

    #промокод-стратегі 
    promo = input("Введіть промокод (або Enter): ").strip()#стріп прибирає пробіли
    discount = di.order_service.apply_discount(order, promo)
    if discount > 0:
        print(f"🎁 Застосовано знижку: {discount}%")
    else:
        print("ℹ️ Знижка не застосована.")

    print(order)

    #оплата-фекторі
    print("\n💳 Спосіб оплати:")
    print("1. Картка")
    print("2. Apple Pay")
    method = validate_int("Ваш вибір (1-2): ", 1, 2)

    payload = {}
    if method == 1:
        payload["card_number"] = validate_card_number()
        payload["exp"] = validate_exp()
        payload["cvv"] = validate_cvv()
    else:
        payload["confirm"] = input("Підтвердіть Apple Pay (напишіть YES): ").strip().upper()

    print("\n🔄 Оплата...")
    paid = di.payment_service.process_payment(order, method, payload)

    #повідомлення-обсервер
    di.notification_service.setup(email, phone)

    if not paid:
        order.status = "FAILED"
        di.notification_service.notify(f"❌ Оплата замовлення №{order.order_number} не вдалася. Спробуйте ще раз.")
        di.repository.save_to_file(order)
        print("❌ Оплата не пройшла. Завершення.")
        return

    order.status = "PAID"
    di.notification_service.notify(f"✅ Оплата успішна! Замовлення №{order.order_number} прийнято.")

    #доставка
    courier, minutes = di.delivery_service.assign_delivery(order)
    order.status = "DELIVERY"
    di.notification_service.notify(f"🚚 Кур'єр: {courier}. Орієнтовний час: {minutes} хв.")

    order.status = "DONE"
    di.notification_service.notify("🍽️ Замовлення доставлено! Смачного ❤️")

    #збереження
    di.repository.save_to_file(order)
    print("\n✅ Замовлення збережено у файл orders.txt")

if __name__ == "__main__":
    main()
