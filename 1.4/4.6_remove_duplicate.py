def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for element in lst:
        if element not in seen:
            unique_lst.append(element)
            seen.add(element)
    return unique_lst


try:
    
    user_input = input("Enter the list of numbers separated by spaces: ")

    lst = [int(x) for x in user_input.split()]
    
    
    unique_lst = remove_duplicates(lst)
    print("Original list:", lst)
    print("Output list (with duplicates removed):", unique_lst)
except ValueError:
    print("Please enter a valid list of numbers.")

    