class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
# Создание магазинов
store1 = Store("Фрукты и Овощи", "ул. Садовая, 1")
store2 = Store("СуперМаркет", "пр. Ленина, 23")
store3 = Store("МиниМаркет", "ул. Победы, 15")

# Добавляем товары
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("bread", 1.2)
store2.add_item("milk", 0.95)

store3.add_item("water", 0.4)
store3.add_item("juice", 1.5)

# Тестирование методов на store1
print("Цена яблок:", store1.get_price("apples"))

store1.update_price("apples", 0.55)
print("Новая цена яблок:", store1.get_price("apples"))

store1.remove_item("bananas")
print("Бананы после удаления:", store1.get_price("bananas"))  # None
