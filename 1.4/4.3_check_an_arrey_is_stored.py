def is_sorted(arr):
   
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


try:
    n = int(input("Enter n: "))
    if n <= 0:
        print("Please enter a positive integer for the length.")
    else:
      
        print("Enter the array elements:")
        arr = []
        for _ in range(n):
            element = int(input())
            arr.append(element)
        
       
        if is_sorted(arr):
            print("The array is sorted.")
        else:
            print("The array is not sorted.")
except ValueError:
    print("Please enter valid integers.")
