MAX_LINES = 3 #defining a constant
MAX_BET = 100
MIN_BET = 1
# a function for depositing money
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet? ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return bet

def main():
    balance = deposit()
    line = get_number_of_lines()
    print(f"Your balance is ${balance}")



main()