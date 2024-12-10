import sys
import time

class myColors :
        
	ResetAll = "\033[0m"

	Bold       = "\033[1m"
	Dim        = "\033[2m"
	Underlined = "\033[4m"
	Blink      = "\033[5m"
	Reverse    = "\033[7m"
	Hidden     = "\033[8m"

	ResetBold       = "\033[21m"
	ResetDim        = "\033[22m"
	ResetUnderlined = "\033[24m"
	ResetBlink      = "\033[25m"
	ResetReverse    = "\033[27m"
	ResetHidden     = "\033[28m"

	Default      = "\033[39m"
	Black        = "\033[30m"
	Red          = "\033[31m"
	Green        = "\033[32m"
	Yellow       = "\033[33m"
	Blue         = "\033[34m"
	Magenta      = "\033[35m"
	Cyan         = "\033[36m"
	LightGray    = "\033[37m"
	DarkGray     = "\033[90m"
	LightRed     = "\033[91m"
	LightGreen   = "\033[92m"
	LightYellow  = "\033[93m"
	LightBlue    = "\033[94m"
	LightMagenta = "\033[95m"
	LightCyan    = "\033[96m"
	White        = "\033[97m"

	BackgroundDefault      = "\033[49m"
	BackgroundBlack        = "\033[40m"
	BackgroundRed          = "\033[41m"
	BackgroundGreen        = "\033[42m"
	BackgroundYellow       = "\033[43m"
	BackgroundBlue         = "\033[44m"
	BackgroundMagenta      = "\033[45m"
	BackgroundCyan         = "\033[46m"
	BackgroundLightGray    = "\033[47m"
	BackgroundDarkGray     = "\033[100m"
	BackgroundLightRed     = "\033[101m"
	BackgroundLightGreen   = "\033[102m"
	BackgroundLightYellow  = "\033[103m"
	BackgroundLightBlue    = "\033[104m"
	BackgroundLightMagenta = "\033[105m"
	BackgroundLightCyan    = "\033[106m"
	BackgroundWhite        = "\033[107m"

# Work Place

allstation = ["Goat","Wolf","Cabbage","Farmer"]
west = []
east = []

g = allstation[0]
w = allstation[1]
c = allstation[2]
f = allstation[3]

west.extend([g, w, c, f])

print("{:{align}{width}}\n".format('GWC Game', align='^', width='120'))

print(f"{myColors.LightGreen}A farmer{myColors.ResetAll} went to a market and purchased {myColors.LightGreen}a wolf{myColors.ResetAll}, {myColors.LightGreen}a goat{myColors.ResetAll}, and {myColors.LightGreen}a cabbage{myColors.ResetAll}. On his way home, {myColors.LightYellow}the farmer came to the bank of a river and rented a boat.{myColors.ResetAll}\n\
{myColors.LightRed}But crossing the river by boat, {myColors.ResetAll}the farmer could carry only himself and a single one of his purchases: {myColors.Black}the wolf, the goat, or the cabbage.\n\
{myColors.LightMagenta}If left unattended together, {myColors.LightRed}the wolf would eat the goat, or the goat would eat the cabbage.\n\
{myColors.LightYellow}The farmer's challenge{myColors.ResetAll} was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.")

print(f"For Information use {myColors.LightRed}'help'{myColors.ResetAll} function")
firstpick = input(f"{myColors.LightGreen}Select First Choise: {myColors.ResetAll}")

if firstpick == "help":
    print(f"You use {myColors.LightGreen}g {myColors.LightCyan}for goat{myColors.ResetAll}, {myColors.LightGreen}w {myColors.LightCyan}for wolf{myColors.ResetAll}, {myColors.LightGreen}c {myColors.LightCyan}for cabbage{myColors.ResetAll}, {myColors.LightGreen}f {myColors.LightCyan}for farmer alone{myColors.ResetAll}")

elif firstpick == "w":
    print(f"You and the wolf crossed over. Right Now, If you want cross over with wolf select {myColors.Black}'w'{myColors.ResetAll} Or you want cross over alone click {myColors.Black}'f'{myColors.ResetAll}")
    secondpick = input(f"{myColors.LightGreen}Select Second Choise: {myColors.ResetAll}")
    if secondpick == "w":
        print(f"You and the wolf crossed over. But {myColors.LightGreen}goat ate cabbage, {myColors.LightRed}mission is failed!{myColors.ResetAll} Another day another chance")
    elif secondpick == "f":
        print(f"{myColors.Cyan}You alone crossed over. But {myColors.LightGreen}goat ate cabbage, {myColors.LightRed}mission is failed!{myColors.ResetAll} Another day another {myColors.LightYellow}chance.{myColors.ResetAll}")
    else:
        a = 0  
        for x in range (0,3):  
            a+= 1  
            b = ("Maybe you should try it again" + "." * a)
            sys.stdout.write('\r'+b)
            time.sleep(0.5)
        print(f" {myColors.BackgroundLightRed}or I thought, never mind!{myColors.ResetAll}")

elif firstpick == "c":
    print(f"You and the cabbage crossed over. Right Now, If you want cross over with cabbage select {myColors.Black}'c'{myColors.ResetAll} Or you want cross over alone click {myColors.Black}'f'{myColors.ResetAll}")
    secondpick = input(f"{myColors.LightGreen}Select Second Choise: {myColors.ResetAll}")
    if secondpick == "c":
        print(f"You and the cabbage crossed over. But {myColors.LightGreen}wolf ate goat, {myColors.LightRed}mission is failed!{myColors.ResetAll} Another day another {myColors.LightYellow}chance.{myColors.ResetAll}")
    elif secondpick == "f":
        print(f"{myColors.Cyan}You alone crossed over. But {myColors.LightGreen}wolf ate goat, {myColors.LightRed}mission is failed!{myColors.ResetAll} Another day another {myColors.LightYellow}chance.{myColors.ResetAll}")
    else:
        a = 0  
        for x in range (0,3):  
            a+= 1  
            b = ("Maybe you should try it again" + "." * a)
            sys.stdout.write('\r'+b)
            time.sleep(0.5)
        print(f" {myColors.BackgroundLightRed}or I thought, never mind!{myColors.ResetAll}")

elif firstpick == "f":
    print(f"You crossed over. Right Now, If you want cross over select {myColors.Black}'f'{myColors.ResetAll} Or you can walk to the village select {myColors.Black}'v'{myColors.ResetAll}")
    secondpick = input(f"{myColors.LightGreen}Select Second Choise: {myColors.ResetAll}")
    if secondpick == "f":
        print(f"You and crossed over alone. But {myColors.LightGreen}goat ate cabbage, wolf ate goat, {myColors.LightRed}mission is failed!{myColors.ResetAll} Another day another {myColors.LightYellow}chance.{myColors.ResetAll}")
    elif secondpick == "v":
        print(f"{myColors.LightBlue} You started walking towards the village,{myColors.ResetAll} after a while you saw that the village was looted and a group of soldiers were walking towards you,\n you tried to run backwards {myColors.LightRed}but they caught you and killed you. {myColors.LightYellow}Sometimes the greatest freedom is the work you have to do.{myColors.ResetAll}")
    else:
        a = 0  
        for x in range (0,3):  
            a+= 1  
            b = ("Maybe you should try it again" + "." * a)
            sys.stdout.write('\r'+b)
            time.sleep(0.5)
        print(f" {myColors.BackgroundLightRed}or I thought, never mind!{myColors.ResetAll}")


elif firstpick == "g":
    print(f"You and the goat crossed over. Right Now, If you want cross over with goat select {myColors.Black}'g'{myColors.ResetAll} Or you want cross over alone click {myColors.Black}'f'{myColors.ResetAll}")
    secondpick = input(f"{myColors.LightGreen}Select Second Choise: {myColors.ResetAll}")
    if secondpick == "g":
        print(f"You and the goat crossed over. But {myColors.LightGreen}the situation was the same as before, {myColors.LightYellow}try again.{myColors.ResetAll}")
        secondpick = input(f"{myColors.LightGreen}Select Second Choise: {myColors.ResetAll}")
    elif secondpick == "f":
        print(f"You and crossed over alone. Right now {myColors.LightGreen}you can select wolf or cabbage, for wolf {myColors.Black}'w'{myColors.ResetAll} for cabbage {myColors.Black}'c'{myColors.ResetAll}")
        thirdpick = input(f"{myColors.LightGreen}Select Second Choise: {myColors.ResetAll}")
        if thirdpick == "c":
            print(f"You and the cabbage crossed over. Right Now, you can select goat, cabbage or alone {myColors.LightGreen}wolf ate goat, {myColors.LightRed}mission is failed!{myColors.ResetAll} Another day another {myColors.LightYellow}chance.{myColors.ResetAll}")
    else:
        a = 0  
        for x in range (0,3):  
            a+= 1  
            b = ("Maybe you should try it again" + "." * a)
            sys.stdout.write('\r'+b)
            time.sleep(0.5)
        print(f" {myColors.BackgroundLightRed}or I thought, never mind!{myColors.ResetAll}")

else:
	a = 0  
	for x in range (0,3):
		a+= 1
		b = ("Maybe you should try it again" + "." * a)
		# \r prints a carriage return first, so `b` is printed on top of the previous line.
		sys.stdout.write('\r'+b)
		time.sleep(0.5)
	print(f" {myColors.BackgroundLightRed}or I thought, never mind!{myColors.ResetAll}")





# thirdpick create

