import random

class Hangman:
    """
    A class to represent the Hangman game.

    Attributes:
        word_list (list): List of words to choose from.
        num_lives (int): Number of lives the player has.
        word (str): The word to guess, chosen randomly from word_list.
        word_guessed (list): A list of guessed letters, initially all underscores.
        num_letters (set): A set of unique letters in the word.
        list_of_guesses (list): A list of letters guessed by the player.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Constructs all the necessary attributes for the Hangman object.

        Parameters:
            word_list (list): List of words to choose from.
            num_lives (int): Number of lives the player has. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = set(list(self.word))
        self.list_of_guesses = []

   
    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        Parameters:
            guess (str): The guessed letter.
        """    
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
            print(f"You have {self.num_lives} lives left.")
            


    def ask_for_input(self):
        """
        Continously asks player for input until a valid guess is made
        """
        while True:
            print(self.word_guessed)
            guess = input("Please enter a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character: ")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
        

def play_game(word_list):
    """
    Plays a game of Hangman.

    Parameters:
        word_list (list): List of words to choose from.
    """
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print ("You lost!")
            break
        elif len(game.num_letters) > 0:
            game.ask_for_input()
        else:
            print(game.word_guessed)
            print("Congratulations. You have won!")
            break

fruit_words = ["aaple", "pear", "banana", "mango", "melon"]
play_game(fruit_words)

