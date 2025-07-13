#ai.py
import time
import re
import random
from datetime import datetime
import webbrowser
import os

from slot_game import SlotGame
from search import search
from quiz_game import quiz
from guess_game import guessing_game
from interest import calculate_compound_interest

def AI(a):
    msg = a.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        print("......")
        time.sleep(1)
        print("Hello, sir. How can I help you now?")
    
    elif msg == "search":
        search()

    elif "add" in msg:
        numbers = re.findall(r'\d+', a)
        if len(numbers) >= 2:
            numbers = [int(num) for num in numbers]
            print(f"The result is: {sum(numbers)}")
        else:
            print("Please provide at least two numbers to add.")

    elif "subtract" in msg:
        numbers = re.findall(r'\d+', a)
        if len(numbers) >= 2:
            result = int(numbers[0]) - int(numbers[1])
            print(f"The result is: {result}")
        else:
            print("Please provide two numbers to subtract.")

    elif "multiply" in msg:
        numbers = re.findall(r'\d+', a)
        if len(numbers) >= 2:
            result = int(numbers[0]) * int(numbers[1])
            print(f"The result is: {result}")
        else:
            print("Please provide two numbers to multiply.")

    elif "divide" in msg:
        numbers = re.findall(r'\d+', a)
        if len(numbers) >= 2 and int(numbers[1]) != 0:
            result = int(numbers[0]) / int(numbers[1])
            print(f"The result is: {result}")
        else:
            print("Provide valid numbers. Cannot divide by 0.")

    elif "interest" in msg or "compound" in msg:
        calculate_compound_interest()

    elif "quiz" in msg:
        time.sleep(.9)
        print("OK,✌️ Let's play a quiz game:")
        quiz()

    elif "guess" in msg:
        time.sleep(.9)
        print("OK,✌️ Let's play the guessing game:")
        guessing_game()

    elif "play slot" in msg:
        game = SlotGame()
        game.play()

    elif "time" in msg:
        now = datetime.now()
        print("Current time is:", now.strftime("%H:%M:%S"))

    elif "date" in msg:
        today = datetime.now()
        print("Today's date is:", today.strftime("%Y-%m-%d"))

    elif "open google" in msg:
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in msg:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
        
    elif "open chatgpt" in msg:
        print("Opening ChatGPT...")
        webbrowser.open("https://chatgpt.com")

    elif "joke" in msg:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems.",
            "I told my computer I needed a break, and now it won’t stop sending me KitKat ads."
        ]
        print(random.choice(jokes))

    elif "flip a coin" in msg:
        result = random.choice(["Heads", "Tails"])
        print("Flipping a coin... It's", result)

    elif "clear screen" in msg:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Screen cleared.")

    elif msg == "exit":
        print("Exiting... Have a great day, Sir!")
        exit()

    else:
        print("Sorry, I don't understand that yet. Try something else!")
