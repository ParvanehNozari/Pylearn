def main():
    total=0
    numbers=[]
    
    while True:
        user_input = (input("print: "))
        if user_input == "exit":
            break
        elif user_input.isdigit():
            number = float(user_input)
            numbers.append(number)
            total += number
        else:
            print(" adad e motabar vared konid")
    print("list e aadad: ", numbers)
    print("majmue nahayi: ", total)
    print("finish")
    
print(main())