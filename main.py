import random


class DungeonCrawler:

    def __init__(self):
        self.player_hp = 100
        self.outsmarted = 100
        self.inventory = []
        self.dungeon_size = 10
        self.current_room = 0
        self.coins = 0
        self.is_running = True

    def generate_room_content(self):

        roll = random.random()

        if roll < 0.3: return "Monster"
        if roll < 0.5: return "Treasure"
        if roll < 0.7: return "Trap"
        if roll < 1.0: return "Riddle"

        return "Empty"

    def handle_encounter(self, content):

        if content == "Monster":
            print("(!) A wild AI-generated Grue appears!")
            self.player_hp -= 30

        elif content == "Treasure":
            print("($) You found a Gold Coin!")
            self.coins += 1

        elif content == "Trap":
            print("(X) You stepped on a spike!")
            self.player_hp -= 10

        elif content == "Riddle":
            if self.give_riddle():
                self.player_hp += 50
            else:
                self.outsmarted -= 50

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

def give_riddle():
    num = random.randint(0, 14)
    prompt = RIDDLES.keys()[num]
    print(f"{prompt}!")
    guesses = 0
    correct = False

    while guesses < 3 or correct:
        answer = input(f"{3 - guesses} guesses left. Enter your guess: ")
        if not (answer == RIDDLES[prompt]):
            print(f"Incorrect. Try again. ")
            guesses += 1
        else:
            correct = True

    return correct

if __name__ == "__main__":
    game = DungeonCrawler()
    game.play()