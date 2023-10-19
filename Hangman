import random

def choose_word():
    words = ["candidate", "hangman", "programming", "laptop","science", "computer", "developer", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in word_to_guess:
                print("Correct!")
                guessed_letters.append(guess)
            else:
                print("Incorrect!")
                guessed_letters.append(guess)
                attempts -= 1
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

hangman()
