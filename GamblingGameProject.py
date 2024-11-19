# Noah Phillips 10-30-24
# Basic beginnings for gambling game, 2500 starting cash with 500 dollar spins. Double payout if the player wins.

import random

def gambling_game():
    # starting balance and initial bet amount
    balance = 2500
    bet = 500
    payout_multiplier = 1  # this multiplier doubles after each win

    print("Welcome to the Gambling Game!")
    print(f"Starting balance: ${balance}")
    print(f"Each spin costs ${bet}")

    while balance >= bet:
        # deduct the bet from balance at the start of each round
        balance -= bet
        print(f"\nYou bet ${bet}. Current balance: ${balance}")

        # game: guessing a number between 1 and 10
        guess = int(input("Guess a number between 1 and 10: "))
        winning_number = random.randint(1, 10)

        # determine if the player won or lost
        if guess == winning_number:
            winnings = bet * payout_multiplier * 2
            balance += winnings
            print(f"Congratulations! You guessed correctly and won ${winnings}.")
            print(f"New balance: ${balance}")
            payout_multiplier *= 2  # double the multiplier after a win
        else:
            print(f"Sorry, the winning number was {winning_number}.")
            print(f"New balance: ${balance}")
            payout_multiplier = 1  # reset the multiplier after a loss

        # check if the player wants to continue or quit
        choice = input("Do you want to spin again? (y to continue, anything else to quit): ").strip().lower()
        if choice != "y":
            print(f"You are leaving with ${balance}. Thanks for playing!")
            break

    if balance < bet:
        print("You do not have enough balance to continue. Game over!")

# start the game
gambling_game()
