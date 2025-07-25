
shopping_list = []

def add_item():
    add = "yes"
    while add.lower() == "yes":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
        add = input("Do you want to add more items? (yes/no): ").lower()

    
def remove_item():
    remove = "yes"
    while remove.lower() == "yes":
        item = input("Enter item to remove from shopping list: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
        remove = input("Do you want to remove more items? (yes/no): ").lower()

def view_items():
    for item in shopping_list:
        print(item)

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    global shopping_list 
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item()

        elif choice == 2:
            remove_item()

        elif choice == 3:
            view_items()

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()