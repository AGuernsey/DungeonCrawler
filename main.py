import random


class DungeonCrawler:

    def __init__(self):

        self.player_hp = 100

        self.inventory = []

        self.dungeon_size = 10

        self.current_room = 0

        self.is_running = True

    def generate_room_content(self):

        roll = random.random()

        if roll < 0.3: return "Monster"

        if roll < 0.5: return "Treasure"

        if roll < 0.7: return "Trap"

        return "Empty"

    def handle_encounter(self, content):

        if content == "Monster":

            print("(!) A wild AI-generated Grue appears!")

            self.player_hp -= 30

        elif content == "Treasure":

            print("($) You found a Gold Coin!")

            self.inventory.append("Gold")

        elif content == "Trap":

            print("(X) You stepped on a spike!")

            self.player_hp -= 10

    def play(self):

        print("--- Welcome to the 'Smart' Dungeon ---")

        while self.is_running and self.current_room < self.dungeon_size:

            print(f"\nRoom {self.current_room} | HP: {self.player_hp}")

            content = self.generate_room_content()

            self.handle_encounter(content)

            if self.player_hp <= 0:
                print("GAME OVER: The AI outsmarted you (or just killed you).")

                self.is_running = False

            self.current_room += 1

        if self.player_hp > 0:
            print(f"\nVictory! You finished with {len(self.inventory)} gold.")


if __name__ == "__main__":
    game = DungeonCrawler()

    game.play()