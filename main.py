import random

#constant to define max number of slot lines
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 2


#ask the user for a deposit of money
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        #check for valid whole number and convert string to int
        if amount.isdigit():
            amount = int(amount)
            #exit loop and return amount if greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount of money.")

    return amount

#allow the user to select the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        #check for valid whole number and convert string to int
        if lines.isdigit():
            lines = int(lines)
            #exit loop and return lines if between 1 and 3
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet? $")
        #check for valid whole number and convert string to int
        if bet.isdigit():
            bet = int(bet)
            #exit loop and return bet if between $2 and $100
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid amount of money.")

    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    #check if total bet is less than or equal to balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}.")
    

main()