def reverse_list(lst):
    
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


try:
    
    user_input = input("Enter the list of numbers separated by spaces: ")
    
    lst = [int(x) for x in user_input.split()]
    
    
    reversed_lst = reverse_list(lst)
    print("Original list:", lst)
    print("Reversed list:", reversed_lst)
except ValueError:
    print("Please enter a valid list of numbers.")
