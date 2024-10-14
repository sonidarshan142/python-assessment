# fruit_manager.py
import os

class FruitManager:
    def __init__(self, file_name="fruit_stock.txt"):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                file.write("") 

    def load_stock(self):
        stock = {}
        with open(self.file_name, 'r') as file:
            for line in file:
                if line.strip():
                    fruit, quantity = line.strip().split(',')
                    stock[fruit] = float(quantity)
        return stock

    def save_stock(self, stock):
        with open(self.file_name, 'w') as file:
            for fruit, quantity in stock.items():
                file.write(f"{fruit},{quantity}\n")

    def view_stock(self):
        stock = self.load_stock()
        if not stock:
            print("No fruits available in the stock.")
        else:
            print("Fruit Stock:")
            for fruit, quantity in stock.items():
                print(f"{fruit}: {quantity} kg")

    def add_fruit(self, fruit_name, quantity):
        stock = self.load_stock()
        if fruit_name in stock:
            stock[fruit_name] += quantity
        else:
            stock[fruit_name] = quantity
        self.save_stock(stock)
        print(f"Added {quantity} kg of {fruit_name} to the stock.")

    def update_fruit(self, fruit_name, quantity):
        stock = self.load_stock()
        if fruit_name in stock:
            stock[fruit_name] = quantity
            self.save_stock(stock)
            print(f"Updated {fruit_name} stock to {quantity} kg.")
        else:
            print(f"{fruit_name} not found in stock.")
