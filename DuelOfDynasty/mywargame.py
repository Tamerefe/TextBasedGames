from colorama import Fore, Style, init
import random

# Initialize colorama
init(autoreset=True)

# Define Characters with their attributes
chlst = {
    "Ninja": {
        "Power": random.randint(450, 550),
        "Hp": random.randint(3000, 3500),
        "Heal": 0,
        "Dodge": 25,  # Percentage
        "Name": "Ninja"
    },
    "Gunsmith": {
        "Power": random.randint(850, 1050),
        "Hp": random.randint(1400, 2000),
        "Heal": 0,
        "Dodge": 16,
        "Name": "Gunsmith"
    },
    "Fighter": {
        "Power": random.randint(275, 325),
        "Hp": random.randint(5000, 6000),
        "Heal": 0,
        "Dodge": 14,
        "Name": "Fighter"
    },
    "Healer": {
        "Power": random.randint(150, 200),
        "Hp": random.randint(2200, 3200),
        "Heal": random.randint(375, 525),
        "Dodge": 9,
        "Name": "Healer"
    },
    "Magician": {
        "Power": random.randint(325, 400),
        "Hp": random.randint(2250, 2750),
        "Heal": random.randint(100, 150),
        "Dodge": 33,
        "Name": "Magician"
    }
}

# List of opponents excluding the player
lgt = [chlst['Gunsmith'], chlst['Fighter'], chlst['Healer'], chlst['Ninja'], chlst['Magician']]

def hit(shooter, target):
    """Apply damage to the target based on shooter's power."""
    target["Hp"] -= shooter["Power"]
    print(f"{Fore.RED}{shooter['Name']} hits {target['Name']} for {shooter['Power']} damage!{Style.RESET_ALL}")

def can_heal(healer, target):
    """Apply healing to the target based on healer's heal power."""
    target["Hp"] += healer["Heal"]
    print(f"{Fore.GREEN}{healer['Name']} heals for {healer['Heal']} HP!{Style.RESET_ALL}")

def attempt_dodge(attacker):
    """Determine if the attacker dodges the attack based on Dodge percentage."""
    dodge_chance = random.randint(1, 100)
    if dodge_chance <= attacker["Dodge"]:
        print(f"{Fore.CYAN}{attacker['Name']} dodged the attack!{Style.RESET_ALL}")
        return True
    return False

def select_character():
    """Prompt the user to select a character."""
    print(Fore.WHITE + Style.BRIGHT + """
        Select Your Character

    N) Ninja
    G) Gunsmith
    F) Fighter
    H) Healer
    M) Magician

    """ + Style.RESET_ALL)
    choicS = input("Enter the Character Initial: ").lower()
    mapping = {
        'n': 'Ninja',
        'g': 'Gunsmith',
        'f': 'Fighter',
        'h': 'Healer',
        'm': 'Magician'
    }
    return mapping.get(choicS, None)

def combat(player, opponent):
    """Handle the combat between player and opponent."""
    print(f"\n{Fore.YELLOW}Our war begins between {player['Name']} and {opponent['Name']}!{Style.RESET_ALL}")
    while player["Hp"] > 0 and opponent["Hp"] > 0:
        input(f"\nPress {Style.BRIGHT}'Enter'{Style.RESET_ALL} to proceed to the next round...")
        print(f"{Fore.WHITE}{'-'*50}{Style.RESET_ALL}")

        # Player's turn
        action = 'attack'
        if player["Heal"] > 0:
            action = input(f"Choose action for {player['Name']} - (A)ttack or (H)eal: ").lower()
            if action == 'h':
                can_heal(player, player)
            elif action == 'a':
                if not attempt_dodge(opponent):
                    hit(player, opponent)
            else:
                print(f"{Fore.RED}Invalid action! Defaulting to attack.{Style.RESET_ALL}")
                if not attempt_dodge(opponent):
                    hit(player, opponent)
        else:
            if not attempt_dodge(opponent):
                hit(player, opponent)

        # Check if opponent is defeated
        if opponent["Hp"] <= 0:
            print(f"\n{Fore.YELLOW}{player['Name']} Wins!{Style.RESET_ALL}")
            break

        # Opponent's turn
        # Simple AI: Healer and Magician might choose to heal, others attack
        if opponent["Heal"] > 0:
            # 50% chance to heal
            if random.choice([True, False]):
                can_heal(opponent, opponent)
            else:
                if not attempt_dodge(player):
                    hit(opponent, player)
        else:
            if not attempt_dodge(player):
                hit(opponent, player)

        # Check if player is defeated
        if player["Hp"] <= 0:
            print(f"\n{Fore.YELLOW}{opponent['Name']} Wins!{Style.RESET_ALL}")
            break

        # Check for draw
        if player["Hp"] <= 0 and opponent["Hp"] <= 0:
            print(f"\n{Fore.MAGENTA}Both {player['Name']} and {opponent['Name']} have fallen. It's a Draw!{Style.RESET_ALL}")
            break

        # Display current health
        print(f"{Fore.GREEN}{player['Name']}'s Health: {player['Hp']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{opponent['Name']}'s Health: {opponent['Hp']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'-'*50}{Style.RESET_ALL}")

def combat_1_vs_2(player, opponents):
    """Handle the combat between player and two opponents."""
    print(f"\n{Fore.YELLOW}Our war begins between {player['Name']} and {opponents[0]['Name']} & {opponents[1]['Name']}!{Style.RESET_ALL}")
    while player["Hp"] > 0 and (opponents[0]["Hp"] > 0 or opponents[1]["Hp"] > 0):
        input(f"\nPress {Style.BRIGHT}'Enter'{Style.RESET_ALL} to proceed to the next round...")
        print(f"{Fore.WHITE}{'-'*50}{Style.RESET_ALL}")

        # Player's turn
        action = 'attack'
        if player["Heal"] > 0:
            action = input(f"Choose action for {player['Name']} - (A)ttack or (H)eal: ").lower()
            if action == 'h':
                can_heal(player, player)
            elif action == 'a':
                target_index = int(input(f"Choose target to attack - (0) {opponents[0]['Name']} or (1) {opponents[1]['Name']}: "))
                target = opponents[target_index]
                if target["Hp"] > 0 and not attempt_dodge(target):
                    hit(player, target)
            else:
                print(f"{Fore.RED}Invalid action! Defaulting to attack.{Style.RESET_ALL}")
                target_index = int(input(f"Choose target to attack - (0) {opponents[0]['Name']} or (1) {opponents[1]['Name']}: "))
                target = opponents[target_index]
                if target["Hp"] > 0 and not attempt_dodge(target):
                    hit(player, target)
        else:
            target_index = int(input(f"Choose target to attack - (0) {opponents[0]['Name']} or (1) {opponents[1]['Name']}: "))
            target = opponents[target_index]
            if target["Hp"] > 0 and not attempt_dodge(target):
                hit(player, target)

        # Check if all opponents are defeated
        if all(opponent["Hp"] <= 0 for opponent in opponents):
            print(f"\n{Fore.YELLOW}{player['Name']} Wins!{Style.RESET_ALL}")
            break

        # Opponents' turn
        for opponent in opponents:
            if opponent["Hp"] > 0:
                if opponent["Heal"] > 0:
                    # 50% chance to heal
                    if random.choice([True, False]):
                        can_heal(opponent, opponent)
                    else:
                        if not attempt_dodge(player):
                            hit(opponent, player)
                else:
                    if not attempt_dodge(player):
                        hit(opponent, player)

        # Check if player is defeated
        if player["Hp"] <= 0:
            print(f"\n{Fore.YELLOW}{opponents[0]['Name']} & {opponents[1]['Name']} Win!{Style.RESET_ALL}")
            break

        # Check for draw
        if player["Hp"] <= 0 and all(opponent["Hp"] <= 0 for opponent in opponents):
            print(f"\n{Fore.MAGENTA}Both {player['Name']} and the opponents have fallen. It's a Draw!{Style.RESET_ALL}")
            break

        # Display current health
        print(f"{Fore.GREEN}{player['Name']}'s Health: {player['Hp']}{Style.RESET_ALL}")
        for opponent in opponents:
            print(f"{Fore.GREEN}{opponent['Name']}'s Health: {opponent['Hp']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'-'*50}{Style.RESET_ALL}")

def show_character_skills():
    """Display the skills of all characters."""
    print("\nCharacter Skills:\n")
    for char in chlst.values():
        print(f"{Fore.WHITE}{char['Name']}:\n"
              f"  {Fore.YELLOW}Power: {char['Power']}\n"
              f"  {Fore.GREEN}Hp: {char['Hp']}\n"
              f"  {Fore.RED}Heal: {char['Heal']}\n"
              f"  {Fore.CYAN}Dodge: {char['Dodge']}%\n")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print(Fore.WHITE + Style.BRIGHT + """
                                    Welcome to My Python War Game o7

        1) 1 Vs 1
        2) 1 Vs 2
        3) 2 Vs 2
        4) Character Skills
        Q) Quit
        """ + Style.RESET_ALL)

        choic = input("Enter the Transaction Number: ").lower()

        if choic == "1":
            selected = select_character()
            if selected:
                player = chlst[selected].copy()  # Use copy to prevent modifying original stats
                opponent = random.choice([ch for ch in lgt if ch["Name"] != selected]).copy()
                combat(player, opponent)
            else:
                print(f"{Fore.RED}Invalid character selection!{Style.RESET_ALL}")
        elif choic == "2":
            selected = select_character()
            if selected:
                player = chlst[selected].copy()  # Use copy to prevent modifying original stats
                opponents = random.sample([ch for ch in lgt if ch["Name"] != selected], 2)
                opponents = [opponent.copy() for opponent in opponents]
                combat_1_vs_2(player, opponents)
            else:
                print(f"{Fore.RED}Invalid character selection!{Style.RESET_ALL}")
        elif choic == "3":
            print("BB Daha Sonra Tekrar Bekleriz...")
        elif choic == "4":
            show_character_skills()
        elif choic == "q":
            print("BB Daha Sonra Tekrar Bekleriz...")
            break
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main_menu()
