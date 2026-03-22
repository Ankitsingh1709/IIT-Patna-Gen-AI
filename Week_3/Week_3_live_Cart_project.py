# Shopping Cart System
# still need to intrgate the remove to the Json we are storing

import json
import os

cart = []


def add_items():
    while True:
        try:
            print("\nAdd Item To Cart")
            name = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
        except ValueError as e:
            print("the price entered is not correct try again:")
            continue
        item = {name: price}
        cart.append(item)
        print("\nItem Added To Cart")
        save_cart()

        more = input("Do you want to add more items? (yes/no): ").lower()
        if more != "yes":
            break


def save_cart():
    with open("cart.json", "w") as files:
        json.dump(cart, files, indent= 4)

def load_cart():
    global cart     # this is done to modify the global variable expenses 
    if os.path.exists("cart.json"):
        with open("cart.json", "r") as file:
            cart = json.load(file)
    else:
        cart = []


def view_cart():
    if len(cart) == 0:
        print("No item in the cart. Please enter the items ")
    else:
        print("\n============Below is the items in the Cart===============")
        for index, item in enumerate(cart, start=1):
            for name, price in item.items():
                print(f"{index}. {name} -> Rs.{price}")


def remove_item():
    while True:
        if len(cart) == 0:
            print("Cart is empty. Nothing to remove.")
            break

        view_cart()

        try:
            user_input = int(input("Enter the index of the item to remove: "))
            if user_input < 1 or user_input > len(cart):
                print("Invalid index. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        item_to_delete = cart[user_input - 1]
        permission = input(
            f"Are you sure you want to delete {item_to_delete}? (yes/no): "
        ).lower()

        if permission == "yes":
            cart.pop(user_input - 1)
            print("Item removed.")
        else:
            print("Item not removed.")

        more = input("Do you want to delete more items? (yes/no): ").lower()
        if more != "yes":
            break


def calculate_total():
    total = 0
    for item in cart:
        for price in item.values():
            total += price
    print(f"\nTotal Bill: Rs.{total}")


def most_expensive():
    if len(cart) == 0:
        print("\nCart is empty")
        return
    expensive_price = 0
    expensive_item = None
    for item in cart:
        for name, price in item.items():
            if price > expensive_price:
                expensive_price = price
                expensive_item = name

    print(
        f"\nMost expensive item in your cart is: {expensive_item} -> Rs.{expensive_price}"
    )


def menu():
    while True:
        load_cart()
        print("========== Shooping Cart ========")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Total Bill")
        print("5. Most Expensive Item")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_items()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            most_expensive()
        elif choice == "6":
            print("Exiting the cart byee byee!")
            break
        else:
            print("Invalid choice! Try again")


menu()
