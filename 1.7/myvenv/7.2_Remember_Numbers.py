import random 
import time 
import os 

print("Hello")
print("Welcome to the Remember Numbers Game!")
print("Try to remember the sequence of numbers and repeat it.")
print("The sequence will get longer each round, let's see how far you can go!")
print("Type 'quit' anytime to stop playing!")
print("Type 'reset' anytime to start a new game!")
print("Let's start")

sequence=[]
round_number = 1

while True:
    print("Round", round_number)

    new_number= random.randint(0,9)
    sequence.append(new_number)

    print("Remember this sequence.")
    print(sequence)

    sleep_time = max(1, 6 - round_number)
    time.sleep(sleep_time)

    if os.name=="nt": #windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")

    print(" Now enter the sequence number by number:")
    player_sequence=[]    
    for i in  range(len(sequence)):
        user_input=input().lower()
            
        if user_input == "quit":
            print("Thanks for playing! See you next time!")
            exit()
        elif user_input == "reset":
                print("Game reset! Starting a new game.")
                sequence = []  
                round_number = 1 
                break      
        else:
            player_sequence.append(int(user_input))

    if player_sequence == sequence:
        print("Corret! Moving to the next round!")   
        round_number += 1
    else:
        print("Oops! That was incorret")     
        print(f"You made it to round {round_number}, Good job!") 
        break       


