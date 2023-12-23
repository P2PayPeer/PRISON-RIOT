import random

class Game:
    def __init__(self):
        self.sanity = 100
        self.evidence = 0
        self.relationship_with_aria = 0
        self.day = 1
        self.has_key = False

    def display_intro(self):
        print("Welcome to 'Forbidden Escape' - A Prison Riot Game (PG version)\n")
        print("You are Prisoner X in the dark world of Raiyaku Penitentiary. Can you survive, uncover the truth, and escape?\n")

    def make_choice(self, options):
        print("\nChoose an option:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = input("Enter your choice: ")
        return choice

    def talk_to_aria(self):
        if self.relationship_with_aria < 20:
            print("\nAria seems distrustful and doesn't share much.")
        elif self.relationship_with_aria < 50:
            print("\nAria opens up a bit more, sharing some useful tips.")
        else:
            print("\nAria trusts you and reveals a crucial secret about the prison.")

        self.relationship_with_aria += random.randint(5, 15)
        self.sanity += random.randint(1, 10)
        if not self.has_key and self.relationship_with_aria > 50:
            print("Aria trusts you enough to give you a key she found. It might be useful.")
            self.has_key = True

    def explore_cell(self):
        print("\nYou explore and find something useful.")
        self.evidence += random.randint(5, 15)
        self.sanity -= random.randint(1, 5)
        if not self.has_key:
            chance = random.randint(1, 10)
            if chance > 8:
                print("You found a rusty key hidden behind a loose brick.")
                self.has_key = True

    def rest(self):
        print("\nResting helps you regain your strength.")
        self.sanity += random.randint(5, 20)

    def check_status(self):
        print(f"\nDay: {self.day}")
        print(f"Sanity: {self.sanity}")
        print(f"Evidence: {self.evidence}")
        print(f"Relationship with Aria: {self.relationship_with_aria}")
        print(f"Key: {'Yes' if self.has_key else 'No'}")

    def random_event(self):
        events = ["You overhear guards talking about a secret passage.",
                  "A riot breaks out, but you manage to stay safe.",
                  "You find a hidden note with important information."]
        print("\nRandom event: " + random.choice(events))

    def solve_puzzle(self):
        print("\nYou find a strange lock with a riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind.'")
        answer = input("Enter your answer: ")
        if answer.lower() == "echo":
            print("\nThe lock opens, revealing a hidden passage.")
            self.evidence += 15
        else:
            print("\nNothing happens. It seems the answer is incorrect.")
            self.sanity -= 5

    def progress_day(self):
        self.day += 1
        self.sanity -= random.randint(5, 10)
        self.random_event()

def main():
    game = Game()
    game.display_intro()

    # Simulate a couple of actions for demonstration.
    game.talk_to_aria()
    game.explore_cell()
    game.solve_puzzle()
    game.check_status()

main()
