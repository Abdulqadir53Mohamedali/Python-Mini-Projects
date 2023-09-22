# Constants for the game's settings
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    """Prompt the user to deposit an amount and validate the input."""
    while True:
        amount = input('What would you like to deposit? £')
        if amount.isdigit():
            amount1 = int(amount)
            if amount1 > 0:
                break
            else:
                print('Amount must be greater than zero')
        else:
            print('Please enter a number')
    return amount1

def lines():
    """Prompt the user to choose the number of lines to bet on and validate the input."""
    while True:
        balance = input(f'How many lines would you like to bet on (1-{MAX_LINES})? ')
        if balance.isdigit():
            lines = int(balance)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines ')
        else:
            print('Please enter a number')
    return lines

def get_bet():
    """Prompt the user for their bet amount and validate the input."""
    while True:
        bet = input('How much would you like to bet? £')
        if bet.isdigit():
            amount = int(bet)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount bet must be between {MIN_BET}-{MAX_BET}')
        else:
            print('Please enter a number')
    return amount

def main():
    """Main game loop."""
    # Get the initial deposit from the user
    balance = deposit()
    # Get the number of lines the user wants to bet on
    lin1 = lines()
    while True:
        # Get the bet amount from the user
        bet = get_bet()
        Total_bet = bet * lin1
        if Total_bet > balance:
            print(f'You do not have enough to bet that amount, your balance is {balance}')
        else:
            break

# Start the game
main()
