import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
       
        self.word_guessed = ["_"] * len(self.word)
       
        self.num_letters = set(list(self.word))
        
        self.list_of_guesses = []

   
    def check_guess(self, guess):    
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
            self.num_letters.remove(guess)
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives -= 1
            print("You have {num_lives} lives left.")
            


    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter: ")
            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character: ")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
            

test_game = Hangman(["apple", "banana"])


print(test_game.ask_for_input())
print(test_game.list_of_guesses)
print(test_game.num_lives)
print(test_game.num_letters)
print(test_game.word_guessed)



