import random


class DungeonCrawler:
    # Dictionary with the riddles available to the user
    RIDDLES = {
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?":
            "echo",
        "The more of this there is, the less you see. What is it?":
            "darkness",
        "I have keys but no locks, space but no room. You can enter, but you can't go outside. What am I?":
            "keyboard",
        "What has to be broken before you can use it?":
            "egg",
        "I’m tall when I’m young, and short when I’m old. What am I?":
            "candle",
        "What can travel around the world while staying in a corner?":
            "stamp",
        "The more you take, the more you leave behind. What are they?":
            "footsteps",
        "What has an eye but cannot see?":
            "needle",
        "What gets wetter the more it dries?":
            "towel",
        "I have branches, but no fruit, trunk, or leaves. What am I?":
            "bank",
        "What runs but never walks, has a mouth but never talks?":
            "river",
        "What has many teeth but cannot bite?":
            "comb",
        "What comes once in a minute, twice in a moment, but never in a thousand years?":
            "m",
        "I shave every day, but my beard stays the same. Who am I?":
            "barber",
        "What can fill a room but takes up no space?":
            "light"
    }

    def __init__(self):
        self.player_hp = 100
        self.outsmarted = 100
        self.inventory = []
        self.dungeon_size = 10
        self.current_room = 0
        self.coins = 0
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
            print("(!) A wild AI-generated Grue appears!")
            self.player_hp -= 30

        elif content == "Treasure":
            print("($) You found a Gold Coin!")
            self.coins += 1

            rand = random.random()

            if rand < 0.1:
                print("(!!) You found a Rare Sword!")
                self.inventory.append("Rare Sword")
            if rand < 0.4:
                print("(+) You found a health potion! +10 health!")
                self.player_hp += 10
            else:
                print("($) You found a Gold Coin!")

        elif content == "Trap":
            print("(X) You stepped on a spike!")
            self.player_hp -= 10

        elif content == "Riddle":
            if self.give_riddle():
                self.player_hp += 50
            else:
                self.outsmarted -= 50

    # Normal run behavior for the game, runs until dead or outsmarted
    def play(self):

        print("--- Welcome to the 'Smart' Dungeon ---")

        while self.is_running and self.current_room < self.dungeon_size:

            print(f"\nRoom {self.current_room} | HP: {self.player_hp} | Coins: {self.coins}")
            content = self.generate_room_content()
            self.handle_encounter(content)

            if self.player_hp <= 0:
                print("GAME OVER: The AI killed you.")
                self.is_running = False
            elif self.outsmarted <= 0:
                print("GAME OVER: The AI has outsmarted you.")
                self.is_running = False

            self.current_room += 1

        if self.player_hp > 0:
            print(f"\nVictory! You finished with {len(self.inventory)} gold.")

    def give_riddle(self):
        num = random.randint(0, 14)
        prompts = list(self.RIDDLES.keys())
        prompt = prompts[num]
        print(f"{prompt}!")
        guesses = 0
        correct = False
    
        while guesses < 3 and not correct:
            answer = input(f"{3 - guesses} guesses left. Enter your guess: ")
            if not (answer == self.RIDDLES[prompt]):
                print(f"Incorrect. Try again. ")
                guesses += 1
            else:
                correct = True

        return correct

if __name__ == "__main__":
    game = DungeonCrawler()
    game.play()