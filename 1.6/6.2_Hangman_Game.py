import random

print("Welcome to Hangman!")

words=["ophone","octopus","cake","giraft","seal","red","olive","bird","notebook","love","hate","today"]

word=random.choice(words)

word_list =["-" for _ in range(len(word))]
tries =5
while tries > 0:
    for letter in word_list:
        print(letter, end=" ")
    if "-"  not in word_list:
        print("\nYou win! ")
        break


    print("\nGuess a letter! ")    
    letter=input().lower()
    

    if letter in word:
        print("✔")
        for i in range(len(word_list)):
            if letter == word[i]:
                word_list[i] = letter

    else:
        print("❌") 
        tries -= 1
    if tries == 0:
        print("You lose.")        
print("The end.")           

