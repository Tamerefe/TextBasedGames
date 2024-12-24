from random import randrange

coinr = randrange(1, 101)

def totalcoin(selected_coin):
    def applycoin(current_total):
        return current_total + selected_coin
    return applycoin

def get_valid_coin():
    while True:
        slctcoin = input("You can select 50c, 25c, 10c, 5c, 1c: ")
        if slctcoin in ("50", "25", "10", "5", "1"):
            return int(slctcoin)
        else:
            print("Invalid input. Please enter one of the following values: 50, 25, 10, 5, 1.")

ttlslctcoin = 0

while True:
    slctcoin = get_valid_coin()
    ttlslctcoin = totalcoin(slctcoin)(ttlslctcoin)
    print(f"Your coin value is {ttlslctcoin}c")

    if ttlslctcoin == coinr:
        print("Congratulations! You won the game.")
        break
    elif ttlslctcoin > coinr:
        print("Sorry, you have exceeded the target value. You lose.")
        break