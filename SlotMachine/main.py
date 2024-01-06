import random
MAX_LINES = 3 #defining a constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
#dictionary
symbol_count ={
    "Cherry": 2,
    "Bell": 4,
    "Lemon": 6,
    "Star": 8
}

def get_slot_machine_spin(rows,cols,symbols):
    #list to add symbols
    all_symbols = []
    #    key     its value       dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
    #can use _ to iterate
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column =[]
        #copying list, : slice operator
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            #append is used to add 
            column.append(value)
        columns.append(column)

#function to print 
def print_slot_machine(columns):
    #transposing
    for row in range(len(columns[0])):
        #If we use ennumrate it keeps track of the number of iterations in a loop
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                #end - add at end
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

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
        bet = input("How much would you like to bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")
    return bet

def main():
    balance = deposit()
    line = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*line
        if total_bet>balance:
            print(f"You don't have enough money to bet that much, your balance is only: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {line} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

main()
