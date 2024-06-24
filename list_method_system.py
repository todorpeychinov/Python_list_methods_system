def index_check(index, lst):
    # Function to check if the index is out of range.
    if index in range(len(lst)):
        return True
    return False


def print_updated_lst(lst):
    print('\nUpdated lst:')
    print(lst)


def is_valid(initial_values):
    # Check if comma consist in the string
    if "," in initial_values:
        # String separated with ','
        parts = initial_values.split(",")
        # Check for all parts if they're not empty
        if all(part.strip() for part in parts):
            return True
    return False


def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    # TODO: Prompt the user for a value to append to the list
    # Use the append() method to add the value to the list
    # Print the updated list
    new_value = input("\nEnter the value to be appended to the list: ")
    lst.append(new_value)

    print_updated_lst(lst)

    return lst


def handle_extend(lst):
    # TODO: Prompt the user for values to extend the list (comma-separated)
    # Use the extend() method to add these values to the list
    # Print the updated list
    new_values_as_string = input('\nEnter the values to be appended to the list (comma_separated): ')

    while not is_valid(new_values_as_string):
        print('\nInvalid values input.')
        new_values_as_string = input('Enter the values to be appended to the list (comma_separated): ')

    new_values = new_values_as_string.split(',')
    lst.extend(new_values)

    print_updated_lst(lst)

    return lst


def handle_insert(lst):
    # TODO: Prompt the user for an index and a value to insert at that index
    # Use the insert() method to add the value at the specified index
    # Print the updated list
    value = input('\nEnter the value that you want to insert: ')
    index = int(input('Enter the index of the value to be inserted: '))

    while not index_check(index, lst):
        print('\nIndex out of range.')
        index = int(input('Enter correct index of the value to be inserted: '))

    lst.insert(index, value)
    print_updated_lst(lst)

    return lst


def handle_remove(lst):
    # TODO: Prompt the user for a value to remove from the list
    # Use the remove() method to delete the first occurrence of the value
    # Handle the case where the value is not found in the list
    # Print the updated list
    value_to_remove = input('\nEnter the value to be removed: ')

    if value_to_remove in lst:
        lst.remove(value_to_remove)
        print_updated_lst(lst)

    else:
        print(f'{value_to_remove} is not in the list.')

    return lst


def handle_pop(lst):
    # TODO: Prompt the user for an index to pop (optional, leave empty to pop last item)
    # Use the pop() method to remove the item at the specified index or the last item if no index is provided
    # Handle the case where the index is out of range
    # Print the updated list
    index = input('\nEnter the index of the value to be removed (leave blank space if you want to remove the last element of the list): ')

    if index == '':
        if lst:
            lst.pop()
            print_updated_lst(lst)
        else:
            print(f'\nList is already empty.')

    else:
        index = int(index)
        if index_check(index, lst):
            lst.pop(index)
            print_updated_lst(lst)
        else:
            print(f'\n{index} is out of range index.')

    return lst


def handle_clear(lst):
    # TODO: Use the clear() method to remove all items from the list
    # Print the updated list
    lst.clear()
    print_updated_lst(lst)
    return lst


def handle_index(lst):
    # TODO: Prompt the user for a value to find its index
    # Use the index() method to find the index of the value
    # Handle the case where the value is not found in the list
    # Print the index of the value
    index = None
    value = input('\nEnter the value whose index you want to know: ')

    if value not in lst:
        print(f'\n{value} is not in the list.')

    else:
        index = lst.index(value)
        print(f'\nIndex of {value} is {index}.')

    return index


def handle_count(lst):
    # TODO: Prompt the user for a value to count its occurrences in the list
    # Use the count() method to count how many times the value appears in the list
    # Print the count of the value
    value = input('\nEnter the value whose count you want to count: ')

    counter = lst.count(value)
    print(f'\nCount of {value} is {counter}.')

    return counter



def handle_sort(lst):
    # TODO: Use the sort() method to sort the list in ascending order
    # Print the updated list
    lst.sort()
    print_updated_lst(lst)
    return lst


def handle_reverse(lst):
    # TODO: Use the reverse() method to reverse the order of the list
    # Print the updated list
    lst.reverse()
    print_updated_lst(lst)
    return lst


def handle_copy(lst):
    # TODO: Use the copy() method to create a shallow copy of the list
    # Print the copied list
    copied_lst = lst.copy()
    print('Copied list: \n', copied_lst)
    return copied_lst


def main():
    initial_values = input("Enter initial list values (comma-separated): ")

    while not is_valid(initial_values):
        initial_values = input("\nInvalid input of the initial values.\nEnter initial list values (comma-separated): ")

    lst = initial_values.split(',')
    print(lst)

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
