seconds =int(input())

hours =seconds//3600
minutes=(seconds%3600)//60
seconds=seconds%60
result= f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print(result)