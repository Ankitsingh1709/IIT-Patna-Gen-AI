# potential add on data filter
# delete old expenses 
# Category sum and report


import json
import os
expenses = []

def add_expense():
    print("Add new expense below:")
    amount = float(input("Enter the expense amount: "))
    category = input("Enter category(Food/Travel/Grocery): ")
    description = input("Enter a short description here: ")

    expense = {
        "amount" : amount,
        "category" : category,
        "description": description
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added succesfully!\n")

def view_expenses():
    print("All expense listed below:\n")

    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return   # if len of this expenses is 0 do not borther about furthure logic (return do this) 
    
# enumerate it take iterable as an argument and you can define the start point but return pair , number and the list.
# eg: for k, v in enumerate(abc): pritn(k, "-->", v)
# will return 1 --> abc  2 --abc 
    for index , expense in enumerate(expenses, start= 1):
        print(f"{index}. RS.{expense["amount"]} | {expense["category"]} | {expense["description"]}")
    print()

def total_spending():
    total = 0 
    for expense in expenses:
        total += expense["amount"]
    print(f"\n Total Spending: {total}")
3

def highest_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return
    highest = expenses[0] # this is list and we are accessing it first member.
    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print(f"\n Highest expense:")
    print(f"Rs.{highest["amount"]} | {highest["category"]} | {highest["description"]}\n")

def save_expenses():
    with open("expense.json", "w") as files:
        json.dump(expenses, files, indent= 4)

def load_expenses():
    global expenses     # this is done to modify the global variable expenses 
    if os.path.exists("expense.json"):
        with open("expense.json", "r") as file:
            expenses = json.load(file)
    else:
        expenses = []



def menu():
    load_expenses()
    while True:
        print("===== Expense Tracker ====\n")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Highest Expense")
        print("5. Exit")

        choice = input("choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            highest_expenses()
        elif choice == "5":
            print("Exiting tracker.......")
            break
        else:
            print("Invalid choice, try again!!")

menu()