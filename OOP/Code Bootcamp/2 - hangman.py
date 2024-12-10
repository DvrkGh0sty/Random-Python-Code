import random

list_words = ['Phone', 'oxford', 'charger', 'programmer']

def main():
    print("Welcome to the Hangman game!")
    
    rand = random.choice(list_words).lower()
    
    blanks = ["_"] * len(rand)
    attempts = 6 
    guessed_letters = [] 

    while attempts > 0 and "_" in blanks:
        print("\n" + " ".join(blanks)) 
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in rand:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(rand):
                if letter == guess:
                    blanks[i] = guess
        else:
            print(f"Oops! {guess} is not in the word.")
            attempts -= 1 


    if "_" not in blanks:
        print("\nCongratulations! You guessed the word:", rand)
    else:
        print("\nGame over! The word was:", rand)

main()
