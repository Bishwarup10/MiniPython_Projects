#SLOT Machine Game

import random


symbols = ["Cherry", "Bell", "Orange", "Star", "Apple", "King"]
payouts = {
    "Cherry": 2,
    "Bell": 5,
    "Orange": 8,
    "Star": 10,
    "Apple": 15,
    "King": 20
}


def display_reels(reels):
    print(" | ".join(reels))


def check_win(reels, bet_amount):
    
    if reels[0] == reels[1] == reels[2]:
        symbol = reels[0]
        payout = payouts[symbol] * bet_amount
        return True, payout
    else:
        return False, 0


def play_slot_machine():
    print("Welcome to the Slot Machine!")
    print("---------------------------")
    
    total_money = 100  
    bet_amount = 0
    
    while total_money > 0:
        print(f"Your current balance: ${total_money}")
        bet_amount = int(input("Place your bet (minimum bet is $1): "))
        
        if bet_amount < 1 or bet_amount > total_money:
            print("Invalid bet amount. Please place a valid bet.")
            continue
        
        total_money -= bet_amount
        
        input("Press Enter to spin the reels...")
        
        reels = [random.choice(symbols) for _ in range(3)]
        
        display_reels(reels)
        
        win, payout = check_win(reels, bet_amount)
        
        if win:
            total_money += payout
            print(f"Congratulations! You win ${payout}!")
        else:
            print("Sorry, you didn't win this round.")
        
        if total_money > 0:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
        else:
            print("You're out of money! Game over.")
            break
    
    print(f"Your final balance: ${total_money}")
    print("Thanks for playing!")

play_slot_machine()
