# slot_game.py
import random
from time import sleep

class SlotGame:
    def spin_row(self):
        symbols = ['🍉','🍎','⭐','🔥']
        return [random.choice(symbols) for _ in range(3)]

    def print_row(self, row):
        print("***************")
        print(" | ".join(row))
        print("***************")

    def get_payout(self, row, bet):
        if row[0] == row[1] == row[2]:
            return bet * {'🍉': 5, '🍎': 10, '⭐': 20, '🔥': 30}[row[0]]
        return 0

    def play(self):
        print("Welcome To Python Slots!")
        balance = input("Enter a Balance to Start: ")
        try:
            balance = float(balance)
        except:
            print("Invalid balance amount.")
            return

        while balance > 0:
            print(f"Balance: {balance}")
            bet = input("Place Bet: ")
            if not bet.replace('.', '', 1).isdigit():
                print("Enter numeric value!")
                continue

            bet = float(bet)
            if bet > balance or bet <= 0:
                print("Invalid bet.")
                continue

            balance -= bet
            row = self.spin_row()
            print("Spinning...")
            sleep(0.3)
            self.print_row(row)
            payout = self.get_payout(row, bet)
            if payout > 0:
                print(f"You WON! {payout}")
            else:
                print("You lost!")
            balance += payout
            if input("Play again? (Y/N): ").lower() != "y":
                break

        print(f"Game over! Final balance: {balance}")
