import time

seconds = int(input("Enter the number of seconds for the countdown: "))

while seconds > 0:
    print(f"{seconds} seconds remaining...")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
