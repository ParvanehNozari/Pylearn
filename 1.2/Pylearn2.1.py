while True:
    a=int(input())
    b=int(input())
    operator=input()

    if operator == "+":
        result=a+b
    elif operator == "-" :
        result=a-b
    elif operator == "*" :
        result=a**b
    elif operator == "/" :
        if b!= 0:
            result = a / b
        else:
            result ="cannot divide by zero"
    elif operator == "exit" :
        break 
    else:
        result="this is not suppurted"     
    print(result)          

