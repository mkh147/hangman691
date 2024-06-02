import random
#Step 1: Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.
word = "apple"


def check_guess(guess):    
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")
            

    

def ask_for_input():
    while True:
        guess = input("Please enter a letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character: ")
    check_guess(guess)

ask_for_input()


