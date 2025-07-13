# guess_game.py
import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    answer = random.randint(1, 100)
    guesses = 0

    while True:
        guess = input("Guess a number (1-100): ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1
            if guess < answer:
                print("Too Low.")
            elif guess > answer:
                print("Too High.")
            else:
                print(f"Correct! It was {answer}. Guesses: {guesses}")
                break
        else:
            print("Please enter a valid number.")
