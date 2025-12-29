from models.dish import Dish

class MenuService:
    def __init__(self):
        self.menu = [
            Dish("Маргарита", 210.50, "Піца"),
            Dish("Пепероні", 240.00, "Піца"),
            Dish("Чізбургер", 170.00, "Бургер"),
            Dish("Паста Карбонара", 190.00, "Паста"),
            Dish("Цезар", 150.00, "Салат"),
            Dish("Суші сет", 320.00, "Суші"),
        ]

    def show_menu(self):
        print("\n🍽️ Меню:")
        for i, dish in enumerate(self.menu, start=1):
            print(f"{i}. {dish}")

    def get_dish_by_index(self, index: int):
        if 1 <= index <= len(self.menu):
            return self.menu[index - 1]
        return None
