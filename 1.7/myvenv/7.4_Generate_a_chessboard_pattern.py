n = int(input("Enter the number of rows (n): "))
m = int(input("Enter the number of columns (m): "))

for i in range(n):  
    row = ""  
    for j in range(m): 
        if (i + j) % 2 == 0:  
            row += "⬜"  
        else:
            row += "⬛"  
    print(row)  
