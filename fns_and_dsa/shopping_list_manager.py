# Shopping List Manager

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def view_list():
    print("Shopping List:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    add_item("Milk")
    add_item("Bread")
    view_list()
    remove_item("Milk")
    view_list()
