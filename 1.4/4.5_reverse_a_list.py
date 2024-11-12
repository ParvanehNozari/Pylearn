user_input = input("Enter the list of numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]
reversed_list = []
for i in range(len(num_list) - 1, -1, -1):
    reversed_list.append(num_list[i])
print(reversed_list)