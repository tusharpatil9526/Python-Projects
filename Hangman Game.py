import random

# List of 5 predefined words
word_list = ["python", "coding", "html", "css", "javascript"]

# Pick a random word from the list
word = random.choice(word_list)

# Variables
guessed_letters = []  # Letters guessed by the player
incorrect_guesses = 0
max_guesses = 6


current_display = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word. You have 6 chances.")
print(" ".join(current_display))


while incorrect_guesses < max_guesses and "_" in current_display:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        
        for i in range(len(word)):
            if word[i] == guess:
                current_display[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess! You have", max_guesses - incorrect_guesses, "guesses left.")

    print(" ".join(current_display))
    print("Guessed letters:", " ".join(guessed_letters))

# Game result
if "_" not in current_display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over. The word was:", word)
