import random

while True:
    randoms = random.randint(1, 9)
    number = int(input("Enter a Number: "))
    print("The Number Was: ", randoms)

    if number == randoms:
        print("Congratulations! You guessed the number!")
    else:
        input("Unlucky! Better luck next time. Press Enter to continue.")
