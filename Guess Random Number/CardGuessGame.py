import random

cards = dict(
    FirstCard = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19},
    SecondCard = {2, 3, 6, 7, 10, 11, 14, 15, 18, 19},
    ThirdCard = {4, 5, 6, 7, 12, 13, 14, 15, 20},
    FourthCard = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20},
    FifthCard = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
    SixthCard = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
)

def guess_number(cards: dict):
    guessed_numbers = set(range(1, 21))
    for card_name, numbers in cards.items():
        print(f"{card_name}: {sorted(numbers)}")
        while True:
            confirmation = input(f"Is the number you are thinking of in the {card_name}? (Y/N): ").strip().upper()
            if confirmation == "Y":
                guessed_numbers &= numbers
                break
            elif confirmation == "N":
                guessed_numbers -= numbers
                break
            else:
                print("Please enter 'Y' or 'N'.")
    return guessed_numbers

print("Think of a number between 1 and 20 and don't tell me!")
print("I will try to guess this number.")

while True:
    guessed_numbers = guess_number(cards)
    if guessed_numbers:
        guess = random.choice(list(guessed_numbers))
        print(f"My guess: {guess}")
        correct = input("Is this number correct? (Y/N): ").strip().upper()
        if correct == "Y":
            print("Great! I guessed the number.")
            break
        else:
            print("Hmm, let me try again.")
    else:
        print("I couldn't find the number you were thinking of. Let's try again.")
