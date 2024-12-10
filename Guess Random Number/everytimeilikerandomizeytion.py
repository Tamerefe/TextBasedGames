from random import randrange

crte = randrange(101)
i = 0

gues = int(input("Guess the random number (between 0 and 100): "))

while True:
    if gues == crte:
        print("Congratulations! {} is the correct number.".format(gues))
        break
    elif gues < crte:
        print('Number too small')
    else:  # gues > crte
        print('Number too large')
    
    i += 1
    if i == 4:
        print("Sorry Buddy Maybe Next Time Try It. The number was {}.".format(crte))
        break
    gues = int(input("Try Again: "))