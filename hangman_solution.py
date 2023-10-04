import random

class HangmanGame:
    '''
    Hangman Game class that manages the game mechanic.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
    num_unique_letters: int
        The number of unique letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    guessed_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word and updates the game state accordingly.
    ask_letter()
        Asks the user for a letter and manages input validation.
    '''
    def __init__(self, word_list, num_lives=5):
        # Initialize attributes as indicated in the docstring
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_unique_letters = len(set(self.word))
        self.num_lives = num_lives
        self.guessed_letters = []
        self.visuals = [
            '''
            __________
              |      |
              |    \ O /
              |      |
              |     /\\
            __|____
            ''',''' 
            __________
              |      |
              |      O
              |      |
              |     /\\
            __|____
            ''','''
             __________
              |      |
              |      O
              |      |
              |     /
            __|____
            ''','''
             __________
              |      |
              |      O
              |      |
              |
            __|____
            ''','''
             __________
              |      |
              |      O
              |
              |
            __|____
            ''']
        
        # Print initialization messages
        print(f"The mystery word has {self.num_unique_letters} characters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word and updates the game state accordingly.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        letter = letter.lower()
        if letter in self.word:
            print(f"The letter {letter} is in the word to be guessed!")
            for index, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[index] = letter
            print(f"Nice! {letter} is in the word!")
            print(f"{self.word_guessed}")
            self.num_unique_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"{self.visuals[self.num_lives]}")
            print(f"You have {self.num_lives} lives left.")
        
        self.guessed_letters.append(letter)

    def ask_letter(self):
        '''
        Asks the user for a letter and manages input validation.
        Calls the check_letter method if the input is valid.
        '''
        while True:
            letter = input("Please enter a letter: ").lower()

            if len(letter) != 1:
                print("Please, enter just one character")
            elif letter in self.guessed_letters:
                print(f"{letter} was already tried")
            else:
                self.check_letter(letter)
                break

def play_game(word_list):
    # Initialize the game
    game = HangmanGame(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_unique_letters > 0:
            game.ask_letter()
        else:
            print("Congratulations! You won!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
