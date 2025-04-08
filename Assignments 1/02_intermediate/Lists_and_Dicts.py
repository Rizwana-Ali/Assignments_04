my_list = ["apple", "mango", "orange", "pear", "apricot"]

def access_element(my_list, index):
    """Return the element at the specified index, or an error message if out of range."""
    if 0 <= index < len(my_list):
        return f'Element at index {index}: {my_list[index]}'
    return "Index out of range"

def modify_element(my_list, index, new_value):
    """Modifies the element at the specified index with the new value."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f'Element at index {index} modified from {old_value} to {new_value}'
    return "Index out of range"

def slice_list(my_list, start, end):
    """Returns a new list containing the elements from the start index to the end index (exclusive)."""
    if 0 <= start <= end <= len(my_list):
        return f'Sliced list: {my_list[start:end]}'
    return "Invalid slice indices!"

def list_game():
    print("\nWelcome to the list manipulation game!")

    my_list = ["apple", "mango", "orange", "pear", "apricot"]

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice List")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                index = int(input("Enter index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Please enter valid inputs.")

        elif choice == "3":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(my_list, start, end))
            except ValueError:
                print("Please enter valid integers.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")


list_game()






















































































































































































