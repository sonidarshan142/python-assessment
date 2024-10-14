# fruit_store.py
import fruit_manager
import logging

# Set up logging for transaction history
logging.basicConfig(filename='transaction_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def display_menu():
    print("\nFruit Store Menu:")
    print("1. View Fruit Stock")
    print("2. Add Fruit to Stock")
    print("3. Update Fruit Stock")
    print("4. Exit")

def handle_menu_choice(choice, fruit_mgr):
    if choice == '1':
        fruit_mgr.view_stock()
    elif choice == '2':
        fruit_name = input("Enter fruit name: ").capitalize()
        try:
            quantity = float(input(f"Enter quantity of {fruit_name} to add (in kg): "))
            fruit_mgr.add_fruit(fruit_name, quantity)
            logging.info(f"Added {quantity} kg of {fruit_name}")
        except ValueError:
            print("Invalid input for quantity. Please enter a numeric value.")
    elif choice == '3':
        fruit_name = input("Enter fruit name: ").capitalize()
        try:
            quantity = float(input(f"Enter new quantity for {fruit_name} (in kg): "))
            fruit_mgr.update_fruit(fruit_name, quantity)
            logging.info(f"Updated {fruit_name} stock to {quantity} kg")
        except ValueError:
            print("Invalid input for quantity. Please enter a numeric value.")
    elif choice == '4':
        print("Exiting the application.")
        return False
    else:
        print("Invalid option. Please try again.")
    return True

def main():
    fruit_mgr = fruit_manager.FruitManager()
    running = True
    while running:
        display_menu()
        choice = input("Enter your choice: ")
        running = handle_menu_choice(choice, fruit_mgr)

if __name__ == "__main__":
    main()
