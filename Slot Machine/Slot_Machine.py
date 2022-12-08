
import random

MAX_DEPOSIT = 1000
MAX_LINES = 3
MIN_BET = 5
MAX_BET = 330
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 5,
    "D": 7,

    }
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,

    }
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

    return winnings, winning_lines

def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
 
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def display_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()





def deposit():
    while True:
        amount = input("Please Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_DEPOSIT:
                break
            else:
                print(f"Please enter amount less then ${MAX_DEPOSIT}")
        else:
            print("Enter a valid amount")
    return amount


def line():
    while True:
        lines = input(f"Please Enter lines from (1-{MAX_LINES}):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                
                break
            else:
                print(f"Maximum number of lines allowed are {MAX_LINES}")
        else:
            print("Enter a valid amount")
    return lines

def get_bet():
    while True:
        amount = input("Please enter bet amount: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Minimum bet allowed is ${MIN_BET} and Maximum bet allowed is ${MAX_BET}")
        else:
            print("Enter a valid amount")
    return amount

def spin_game(balance):
    Line = line()
    
    while True:
        Bet = get_bet()
        total_bet = Bet * Line
        if total_bet > balance :
            print(f"You bid amount exceeds your account balance ${balance} please add balance or go with a low bid")
        else:
            break
    slot = spin(ROWS, COLS, symbol_count)
    display_machine(slot)
    winnings, winning_lines = check_winnings(slot, Line, Bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winning_lines - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to spin(q to quit).")
        if ans == "q":
            break
        balance += spin_game(balance)
    print(f"You left with {balance}")

main()
