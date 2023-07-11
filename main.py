
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

def main():
    balance = deposit()

main()