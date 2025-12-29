from datetime import datetime

class OrderRepository:
    def save_to_file(self, order, filename="orders.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"\n[{datetime.now()}]\n")
            f.write(str(order))
            f.write("\n" + "-"*40 + "\n")
