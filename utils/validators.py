import re

def validate_name(prompt):
    while True:
        name = input(prompt).strip()
        if re.match(r"^[A-Za-zА-Яа-яІіЇїЄєҐґ' -]{2,}$", name):
            return name
        print("❌ Ім’я лише літерами (мінімум 2 символи).")

def validate_phone():
    while True:
        phone = input("Телефон (380XXXXXXXXX): ").strip()
        if re.match(r"^380\d{9}$", phone):
            return phone
        print("❌ Невірно. Формат: 380XXXXXXXXX")

def validate_email():
    while True:
        email = input("Email (лише @gmail.com): ").strip().lower()
        if email.endswith("@gmail.com") and len(email) > 10:
            return email
        print("❌ Пошта має закінчуватись на @gmail.com")

def validate_int(prompt, min_v, max_v):
    while True:
        try:
            x = int(input(prompt))
            if min_v <= x <= max_v:
                return x
            print(f"❌ Введіть число від {min_v} до {max_v}.")
        except ValueError:
            print("❌ Введіть число.")

def validate_card_number():
    while True:
        num = input("Номер картки (16 цифр): ").strip()
        if re.match(r"^\d{16}$", num):
            return num
        print("❌ Має бути 16 цифр.")

def validate_exp():
    while True:
        exp = input("Термін дії (MM/YY): ").strip()
        if re.match(r"^(0[1-9]|1[0-2])/[0-9]{2}$", exp):
            return exp
        print("❌ Невірно. Приклад: 05/27")

def validate_cvv():
    while True:
        cvv = input("CVV (3 цифри): ").strip()
        if re.match(r"^\d{3}$", cvv):
            return cvv
        print("❌ Має бути 3 цифри.")
