n = int(input("Enter the length of the snake: "))

pattern = ""

for i in range(n):
    if i % 2 == 0:
        pattern += "*"  
    else:
        pattern += "#"  

print("Output:", pattern)
