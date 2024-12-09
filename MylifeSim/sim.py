import random

# Random name and country pools
names_male = ["Ahmet", "Mehmet", "Can", "Ali", "Murat"]
names_female = ["Ayşe", "Fatma", "Elif", "Zeynep", "Merve"]
countries = ["Turkey", "Germany", "Japan", "USA", "England"]

# List of random events (Updated for new stats)
events = [
    ("You are getting divorced. For fun, neither spouse leaves the house.", 0, -2000, -20, 0, -10, 0, 0, -5),
    ("Bankruptcy! You only have 200 TL left.", 0, -3000, -30, 0, 0, 0, 0, 0),
    ("A big fire breaks out, your house is damaged.", -40, -5000, -50, 0, -5, -10, 0, 0),
    ("Sick day: You don't go to work/school for a day.", -10, 0, 0, 0, 0, -5, -5, 0),
    ("You adopted a child.", 0, -1000, 20, 0, 10, 0, 0, 0),
    ("You were cheated on!", 0, 0, -30, 0, -15, 0, 0, 0),
    ("You lost your job, you have to choose a new career.", 0, -2000, -20, 0, 0, -20, 0, 0),
    ("You moved to a new house.", 0, -3000, 10, 0, 5, 0, 0, 0),
    ("You redecorated a room in your house.", 0, -500, 15, 0, 0, 0, 0, 10),
    ("Midlife crisis: You spent all your money on fun, clothes, cars.", 0, -5000, 30, 0, 0, 0, 0, 0),
    ("You threw a party!", 0, -1000, 20, 0, 15, 0, 0, 0),
    ("You danced with your family.", 0, 0, 10, 0, 10, 0, 0, 5),
    ("You got a new hairstyle and color.", 0, -500, 5, 0, 0, 0, 0, 0),
    ("You adopted a baby.", 0, -1000, 20, 0, 0, 0, 0, 0),
    ("You skipped school with a friend.", 0, 0, -10, 0, 0, 0, 0, 0),
    ("You threw a pool party.", 0, -500, 15, 0, 10, 0, 0, 5),
    ("You had breakfast, lunch, or dinner with your whole family.", 0, 0, 10, 0, 5, 0, 0, 0),
    ("A firework hit your face.", -20, 0, -10, 0, 0, 0, -10, 0),
    ("You chose a holiday and decorated the house like a holiday.", 0, -500, 20, 0, 5, 0, 0, 0),
    ("You went on vacation.", 0, -3000, 30, 0, 10, 0, 0, 0),
    ("A guest moved into your house.", 0, 0, 10, 0, 10, 0, 0, 0),
    ("You were forcibly conscripted.", -10, 0, 0, 0, 0, 10, 20, 0),
    ("You dueled with someone.", -15, 0, -10, 0, 0, 0, 10, 0),
    ("You were robbed!", 0, -500, -20, 0, 0, -5, 0, 0),
    ("You had a picnic in the park.", 0, -100, 10, 0, 5, 0, 0, 5),
    ("You wrote a book.", 0, 500, 20, 10, 0, 0, 0, 5),  # Intelligence increases
    ("You became an author and earned money from your books.", 0, 1000, 20, 10, 0, 10, 0, 5),  # Intelligence and career increase
    ("You took a freelance job and earned money.", 0, 1500, 20, 0, 0, 15, 0, 0),  # Career increases
    ("You earned money from an online job.", 0, 2000, 15, 0, 0, 10, 0, 0),  # Career increases
    ("You won a big prize from the lottery!", 0, 10000, 40, 0, 0, 0, 0, 0),  # Only money
    ("You made a YouTube video that went viral and earned money.", 0, 3000, 25, 0, 10, 10, 0, 0),  # Social skill and career increase
    ("You invested in the stock market and earned money.", 0, 5000, 30, 0, 0, 15, 0, 0),  # Career increases
    ("You helped a neighbor and got paid.", 0, 800, 15, 0, 10, 0, 0, 5),
    ("You started a business and succeeded, earning money.", 0, 7000, 35, 0, 0, 20, 0, 0),  # Career increases
    ("You ordered food and flirted with the pizza delivery person.", 0, 0, 15, 0, 10, 0, 0, 0),
    ("You invited a neighbor to your house and locked them in a room.", 0, 0, -30, 0, -20, 0, 0, 0),
    ("You went on a date.", 0, -200, 20, 0, 10, 0, 0, 0),
    ("You attended a community event and made new friends.", 0, 0, 20, 0, 10, 0, 0, 0),
    ("You read a self-improvement book, increasing your intelligence and happiness.", 0, 0, 15, 10, 0, 0, 0, 0),  # Intelligence increases
    ("You changed all your clothes and created a new style.", 0, -500, 10, 0, 5, 0, 0, 0),
    ("You caught a fish and hung it on the wall.", 0, -100, 5, 0, 0, 0, 0, 5),  # Hobby increases
    ("You started a YouTube channel and started earning money.", 0, 1000, 20, 0, 10, 15, 0, 0),  # Social skill and career increase
    ("You started a blog and your earnings increased.", 0, 2000, 15, 10, 0, 10, 0, 0),  # Intelligence and career increase
]

class Character:
    def __init__(self):
        # Random gender selection
        self.gender = random.choice(["Male", "Female"])
        
        # Name selection from the pool according to gender
        if self.gender == "Male":
            self.name = random.choice(names_male)
        else:
            self.name = random.choice(names_female)
        
        # Random country selection
        self.country = random.choice(countries)
        
        # Age starts from 0
        self.age = 0  
        
        # Values like Health, Money, Happiness are assigned randomly
        self.health = random.randint(50, 100)  # Health between 50-100
        self.money = random.randint(1000, 10000)  # Money between 1000-10000 TL
        self.happiness = random.randint(20, 80)  # Happiness between 20-80
        self.intelligence = random.randint(0, 100)  # Intelligence between 0-100
        self.social_skill = random.randint(0, 100)  # Social skill between 0-100
        self.career_experience = random.randint(0, 100)  # Career experience between 0-100
        self.physical_strength = random.randint(0, 100)  # Physical strength between 0-100
        self.hobby_skill = random.randint(0, 100)  # Hobby skill between 0-100

    def show_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Gender: {self.gender}")
        print(f"Country: {self.country}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Money: {self.money} TL")
        print(f"Happiness: {self.happiness}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Social Skill: {self.social_skill}")
        print(f"Career Experience: {self.career_experience}")
        print(f"Physical Strength: {self.physical_strength}")
        print(f"Hobby Skill: {self.hobby_skill}")
        print("----------------------------\n")

    def is_alive(self):
        return self.health > 0

class LifeSimulation:
    def __init__(self, character):
        self.character = character
    
    def play_turn(self):
        if not self.character.is_alive():
            print("Your character is not alive. Game over!")
            return False

        self.character.age += 1
        print(f"\nYou turned {self.character.age} years old.")
        
        # Generate random events
        event = random.choice(events)
        self.process_event(event)
        return True
    
    def process_event(self, event):
        description, health_change, money_change, happiness_change, intelligence_change, social_change, career_change, strength_change, hobby_change = event
        print(f"Event: {description}")
        
        # Update character attributes
        self.character.health += health_change
        self.character.money += money_change
        self.character.happiness += happiness_change
        self.character.intelligence += intelligence_change
        self.character.social_skill += social_change
        self.character.career_experience += career_change
        self.character.physical_strength += strength_change
        self.character.hobby_skill += hobby_change
        
        # Check limits
        self.character.health = max(0, min(100, self.character.health))
        self.character.happiness = max(0, min(100, self.character.happiness))
        self.character.intelligence = max(0, min(100, self.character.intelligence))
        self.character.social_skill = max(0, min(100, self.character.social_skill))
        self.character.career_experience = max(0, min(100, self.character.career_experience))
        self.character.physical_strength = max(0, min(100, self.character.physical_strength))
        self.character.hobby_skill = max(0, min(100, self.character.hobby_skill))
        
        # Show character status
        self.character.show_status()

# Main game loop
def main():
    print("Welcome to My Life Simulation!")
    print("Press Enter to continue, type 'q' to quit")
    
    # Create character
    character = Character()
    simulation = LifeSimulation(character)
    
    # Show initial character status
    character.show_status()
    
    # Game loop
    while simulation.play_turn():  # Infinite loop, will exit when 'q' is entered
        user_input = input("Advance the year: ")
        if user_input.lower() == 'q':  # If 'q' is typed, break the loop
            break
    
    print("Game over.")

# Start the game
if __name__ == "__main__":
    main()
