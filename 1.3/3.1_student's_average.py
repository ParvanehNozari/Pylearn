n = int(input("Enter the number of scores: "))
total = 0

for i in range(n):
    score = float(input("Enter student's score: "))
    total += score

average = total / n
print(f"Average: {average}")