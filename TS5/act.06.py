
class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = self.validate_id(item_id)
        self.name = self.validate_name(name)
        self.description = description
        self.price = self.validate_price(price)

    @staticmethod
    def validate_id(item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        return item_id

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        return name.strip()

    @staticmethod
    def validate_price(price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        return price

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def read_item(self, item_id):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            item = self.items[item_id]
            print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")
        except KeyError as e:
            print(f"Error: {e}")

    def update_item(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            if name:
                self.items[item_id].name = Item.validate_name(name)
            if description:
                self.items[item_id].description = description
            if price is not None:
                self.items[item_id].price = Item.validate_price(price)
            print("Item updated successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully.")
        except KeyError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    manager = ItemManager()
    manager.create_item(1, "Laptop", "High performance laptop", 1200.50)
    manager.read_item(1)
    manager.update_item(1, price=1300.75)
    manager.read_item(1)
    manager.delete_item(1)
    manager.read_item(1)