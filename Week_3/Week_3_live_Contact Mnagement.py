# Contact Management System

import json
import os

contacts = {}


def save_contact():
    with open("contact.json", "w") as files:
        json.dump(contacts, files, indent=4)


def load_sontact():
    global contacts  # this is done to modify the global variable expenses
    if os.path.exists("contact.json"):
        with open("contact.json", "r") as file:
            contacts = json.load(file)
    else:
        contacts = {}


def add_contact():
    while True:
        try:
            print("\nAdd New Contact")

            name = input("Enter contact name: ")
            phone = int(input("Enter phone number: "))
        except ValueError as e:
            print("expecting and intiger but got an string")
        contacts[name] = phone

        print(f"Contact {name} added succesfully\n")
        save_contact
        more = input("Do you want to add more contacts? (yes/no)").lower()
        if more != "yes":
            break


def view_contact():
    if len(contacts) == 0:
        print("No contacts found.\n")
    print("\nAll contact in the list is below")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")

    print()

def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print(f"{name}'s Number: {contacts[name]}")
    else:
        print("Contact not found.\n")

def update_contact():
    print("Below are the name in your contacts")
    for key, value in enumerate(contacts):
        print(f"{key} --> {value}")
    choice = input("Enter the name or index to update: ")

    if choice.isdigit():
        index = int(choice)
        if index < 0 or index >= len(contacts):
            print("Invalid choice")
            return
        value = list(contacts.keys())[index]    

        
    else:
        value = choice
        print(f"You updating contact number for {value}")
        new_phone = int(input("Enter new phone number: "))
        contacts[value] = new_phone
        print(f"Contact {value} updated successfully.\n")
        save_contact()

def delete_contact():
    print("Below are the name in your contacts")
    for key, value in enumerate(contacts):
        print(f"{key} --> {value}")
    choice = input("Enter the name or index to delete")

    if choice.isdigit():
        index = int(choice)
        if index < 0 or index >= len(contacts):
            print("Invalid choice")
            return
        name = list(contacts.keys())[index]
    else:
        name = choice

    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.\n")
        save_contact()
    else:
        print("Contact not found.\n")


def menu():
    load_sontact()
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")    

menu()


        



