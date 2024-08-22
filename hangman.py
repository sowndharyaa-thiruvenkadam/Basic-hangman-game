import random
import os
import time

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_hangman_stage(stage):
    # Print the hangman stage
    hangman = [
        """
            _________
           |         |
           |         O
           |        \\|/
           |         |
           |        / \\
           |
        """,
        """
            _________
           |         |
           |         O
           |        \\|/
           |         |
           |        / 
           |
        """,
        """
            _________
           |         |
           |         O
           |        \\|/
           |         |
           |        
           |
        """,
        """
            _________
           |         |
           |         O
           |        \\|
           |         |
           |        
           |
        """,
        """
            _________
           |         |
           |         O
           |         |
           |         |
           |        
           |
        """,
        """
            _________
           |         |
           |         O
           |        
           |         
           |        
           |
        """,
        """
            _________
           |         |
           |         
           |        
           |          
           |          
           |
        """
    ]
    print(hangman[stage])

def play_hangman():
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi', 'watermelon','mango', 'strawberry', 'blueberry','berry','grape', 'grapefruit','apricot','avocado','papaya','cherry','peach','muskmelon','custardapple','lychee','pomegranate']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    success = False

    print("Welcome to Hangman!")
    time.sleep(1)
    print("How to play?\n\tThe computer will think of a random word and keep it a secret.\n\tYou have to figure out the word by guessing one letter at a time.\n\tIf the guessed letter is in the word, it gets revealed in its correct position(s).\n\tIf the guessed letter is not in the word, a part of a stick figure (representing a person) gets drawn.\n\tYou keep guessing letters until you either figure out the word or the stick figure is fully drawn (which means you lose).\n\tThe game ends when the word is guessed correctly or when the stick figure is completed.") 
    input("Press Enter to continue...")
    clear_screen()
    while attempts > 0: 
        print_hangman_stage(6 - attempts)
        print("Word:", end=' ')
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print("\n")

        if all(letter in guessed_letters for letter in word):
            success = True
            break

        
        print("Hint: The secret word may be a fruit")
        print("You need to guess", len(word), "letter word")
        guess = input("Guess a letter: ").lower()
        

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            time.sleep(1)
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            time.sleep(1)
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1

    clear_screen()
    if success:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of attempts. The word was:", word)

# Main loop to allow restarting the game
while True:
    play_hangman()
    restart = input("Do you want to play again? (yes/no): ").lower()
    if restart != 'yes':
        print("Thanks for playing Hangman!")
        break
