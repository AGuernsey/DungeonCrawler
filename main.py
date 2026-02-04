"""
Class: Programming 4
Professor: Dr. Shown
Authors: Abraham Guernsey and Kane McCrory
File name: main.py
"""
import random
import re


class DungeonCrawler:
    # Riddles available to the user
    RIDDLES = [
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "The more of this there is, the less you see. What is it?",
        "I have keys but no locks, space but no room. You can enter, but you can't go outside. What am I?",
        "What has to be broken before you can use it?",
        "I’m tall when I’m young, and short when I’m old. What am I?",
        "What can travel around the world while staying in a corner?",
        "The more you take, the more you leave behind. What are they?",
        "What has an eye but cannot see?",
        "What gets wetter the more it dries?",
        "I have branches, but no fruit, trunk, or leaves. What am I?",
        "What runs but never walks, has a mouth but never talks?",
        "What has many teeth but cannot bite?",
        "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "I shave every day, but my beard stays the same. Who am I?",
        "What can fill a room but takes up no space?"
    ]

    # Answers to riddles
    ANSWERS = [
        ["echo"],
        ["darkness"],
        ["keyboard"],
        ["egg", "eggshell", "shoe", "shoes"],
        ["candle"],
        ["stamp"],
        ["footsteps", "footprints"],
        ["needle"],
        ["towel", "sponge"],
        ["bank"],
        ["river"],
        ["comb"],
        ["\'m\'", "letter m", "letter \'m\'"],
        ["barber", "a barber"],
        ["light", "darkness", "silence"]
    ]

    def __init__(self):
        self.player_hp = 100
        self.player_intel = 100
        self.inventory = []
        self.dungeon_size = 10
        self.current_room = 0
        self.coins = 0
        self.player_defense = 0
        self.is_running = True

    # Generate what the next room will be
    def generate_room_content(self):

        roll = random.random()

        if roll < 0.3: return "Monster"
        if roll < 0.5: return "Treasure"
        if roll < 0.7: return "Trap"
        if roll < 1.0: return "Riddle"

        return "Empty"

    # Handling the different rooms and what each entails
    def handle_encounter(self, content):

        if content == "Monster":
            print(f"(!) A wild AI-generated Grue appears! -{30 - self.player_defense} health!")
            self.player_hp -= (30 - self.player_defense)

        elif content == "Treasure":
            rand = random.random()

            if rand < 0.1:
                print("(!!) You found a Rare Shield! +1 Rare Shield")
                self.inventory.append("Rare Shield")
                self.player_defense += 10
            if rand < 0.4:
                print("(+) You found a health potion! +10 health!")
                self.player_hp += 10
            else:
                print("($) You found a Gold Coin! +1 Gold Coin")
                self.coins += 1

        elif content == "Trap":
            print(f"(X) You stepped on a spike! -{15 - self.player_defense} health!")
            self.player_hp -= (15 - self.player_defense)

        elif content == "Riddle":
            if self.give_riddle():
                self.player_hp += 50
                self.player_intel += 30
                print("+50 health and +30 intelligence for answering correctly!")
            else:
                self.player_intel -= 50
                print("-50 intelligence points for being outsmarted!")

    # Normal run behavior for the game, runs until dead or outsmarted
    def play(self):

        print("--- Welcome to the 'Smart' Dungeon ---")

        while self.is_running and self.current_room < self.dungeon_size:

            print(f"\nRoom {self.current_room + 1} | HP: {self.player_hp} | Intel: {self.player_intel} | Defense: {self.player_defense} | Coins: {self.coins}")
            if len(self.inventory) > 0:
                print(f"Inventory: {self.inventory}")
            content = self.generate_room_content()
            self.handle_encounter(content)

            if self.player_hp <= 0:
                print("GAME OVER: The AI killed you.") # Health <= 0
                self.is_running = False
            elif self.player_intel <= 0:
                print("GAME OVER: The AI has outsmarted you.") # Intelligence <= 0
                self.is_running = False

            self.current_room += 1

        if self.player_hp > 0:
            print(f"\nVictory! You finished with {self.coins} gold.")

    def give_riddle(self):
        num = random.randint(0, 14)
        print(f"(R) You found a RIDDLE room! \nRiddle: {self.RIDDLES[num]}")
        guesses = 0
        correct = False
    
        while guesses < 3 and not correct:
            answer = input(f"{3 - guesses} guesses left. Enter your guess:\n")
            answer = re.sub(r'[^a-zA-Z0-9]', ' ', answer) # Converts to alphanumeric characters only (Keeps spaces)
            answer = answer.lower() # Converts all characters to lowercase
            if not any(answer == a for a in self.ANSWERS[num]):
                print("Incorrect. Try again. ")
                guesses += 1
            else:
                print("Correct!")
                correct = True

        return correct

if __name__ == "__main__":
    game = DungeonCrawler()
    game.play()