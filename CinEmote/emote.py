import emoji
import random

def textToEmote(text):
    return emoji.emojize(text)

movies = {
    "The Lion King": "🦁👑",
    "Finding Nemo": "🔍🐠",
    "Titanic": "🚢💔",
    "Jurassic Park": "🦖🦕",
    "Star Wars": "⭐⚔️",
    "The Matrix": "🕶️🔫",
    "Frozen": "❄️👸",
    "Toy Story": "🤠🧸",
    "Harry Potter": "⚡🧙",
    "The Godfather": "👨‍👦🍝"
}

print("Guess the movie from the emojis!")
movie, emote = random.choice(list(movies.items()))
print(f"Emojis: {emote}")
guess = input("Your guess: ")
if guess.lower() == movie.lower():
    print("Correct!")
else:
    print(f"Wrong! The correct answer was {movie}.")