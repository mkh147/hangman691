import random

#Create a list containing 5 fruits, assign variable name word_list
word_list = ["Apple", "Pear", "Banana", "Mango", "Melon"]
print(word_list)


#using imported module, used the choice function to select random fruit from list, assigned it to word
word = random.choice(word_list)
print(word)

#asking the user for a single letter entry for the game
guess = input("Please enter a single letter: ")


#conditonal check to only accept single letter and alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")

else:
    print("Oops! That is not a valid input.")