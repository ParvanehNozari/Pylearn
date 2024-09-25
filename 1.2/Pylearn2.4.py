import random
computer_guess=random.randint(0,100)
guesses=[]
while True:
    user_guess=int(input("guess a number between 1 and 100:"))
    guesses.append(user_guess)
    if user_guess==computer_guess:
        print(f"congratulation!{computer_guess}in {len(guesses)}tries.")
        break
    elif user_guess >  computer_guess :
        print("Try again! You guessed too high")
    else:
        print("Try again! You guessed too small")    
        

