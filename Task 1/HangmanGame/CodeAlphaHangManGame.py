import random

# List of words to choose from
word_list = ["python", "hangman", "bioinformatics", "database", "programming", "beautiful"]

# Function to select a random word from the word list
def get_random_word(word_list):
    return random.choice(word_list)

# Main game logic
def hangman_game():
    word_to_guess = get_random_word(word_list)
    guessed_letters = set()
    max_incorrect_guesses = 7
    incorrect_guesses = 0

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        display = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print("Word to guess:", display)

        if display == word_to_guess:  # Player wins if all letters are guessed
            print("Congratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ")

        # Simplified validation: check if guess is a single character and between 'a' and 'z'
        if guess in "abcdefghijklmnopqrstuvwxyz" and guess not in guessed_letters:
            if guess in word_to_guess:
                guessed_letters.add(guess)
            else:
                incorrect_guesses += 1
                print(f"Wrong guess! Remaining attempts: {max_incorrect_guesses - incorrect_guesses}")
        else:
            print("Invalid input! Please guess a single alphabetic letter.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over!You Lost! The word was: {word_to_guess}")

# Run the game
hangman_game()
