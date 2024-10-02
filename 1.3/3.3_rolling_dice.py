import random

target_sum = int(input("Enter the target sum between 2 and 12: "))

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    
    print(f"You rolled a {dice1} and a {dice2}. Sum: {total}")
    
    if total == target_sum:
        print("Congratulations!")
        break

