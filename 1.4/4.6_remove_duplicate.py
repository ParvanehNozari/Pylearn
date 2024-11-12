def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for element in lst:
        if element not in seen:
            unique_lst.append(element)
            seen.add(element)
    
    print("Output list (with duplicates removed):", unique_lst)
user_input = input("Enter the list of numbers separated by spaces: ")

valid_input = True
lst = []
for x in user_input.split():
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        lst.append(int(x))
    else:
        valid_input = False
        break

if valid_input:
    print("Original list:", lst)
    remove_duplicates(lst)
else:
    print("Please enter a valid list of numbers.")


    