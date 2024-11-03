a = int(input("Enter a number: "))
factorial = 1
i =1

while factorial<a:
    i+=1
    factorial = factorial*i
        
if factorial == a:
        print("Yes")
else:
        print("No") 

