array_input= int(input("Enter array: "))
if array_input<= 0:
    print("please enter positive number: ")
else:
    array=[]
    for i in range(array_input):
        element = int(input("Enter the array elements: "))
        array.append(element)
def is_sorted(array):
    sorted = True
    for i in range(1,len(array)):
        if array[i] < array [i -1]:
            sorted = False
            break
    return sorted
    
if is_sorted(array):
    print("array is sorted.")
else:
    print("array is not sorted.")


