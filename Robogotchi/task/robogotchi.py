import random
import sys
from typing import Tuple


class Robot:

    games: Tuple[str, str] = ('numbers', 'rock-paper-scissors')

    def __init__(self, name='robot', battery=100, overheat=0, skills=0, boredom=0, rust=0) -> None:
        self.name: str = name
        self.battery: int = battery
        self.overheat: int = overheat
        self.skills: int = skills
        self.boredom: int = boredom
        self.rust: int = rust

    def play(self) -> None:

        while True:

            game: str = input("\nWhich game would you like to play?\n").lower()

            if game not in self.games:
                print("\nPlease choose a valid option: Numbers or Rock-paper-scissors?\n")
                continue

            break

        if game == 'numbers':
            self.numbers()
        else:
            self.rps()

    def numbers(self) -> None:

        wins: int = 0
        losses: int = 0
        draw: int = 0

        while True:

            num: int = random.randint(0, 1000000)
            comp: int = random.randint(0, 1000000)

            while True:

                human: str = input("\nWhat is your number?\n")

                if human == 'exit game':
                    print(f"""
You won: {wins},
The robot won: {losses},
Draws: {draw}.
""")

                    prevb: int = self.boredom
                    prevo: int = self.overheat

                    if self.boredom - 20 >= 0:
                        self.boredom -= 20
                    else:
                        self.boredom = 0
                    if self.overheat + 10 < 100:
                        self.overheat += 10
                    else:
                        self.overheat = 100
                        print(f"The level of overheat reached 100, {self.name} has blown up!")
                        print("Game over. Try again?")
                        sys.exit()

                    print(f"{self.name}'s level of overheat was {prevo}. Now it is {self.overheat}.")
                    print(f"{self.name}'s level of boredom was {prevb}. Now it is {self.boredom}.")

                    if self.boredom == 0:
                        print(f"\n{self.name} is in a great mood!")

                    return

                try:
                    human: int = int(human)
                except ValueError:
                    print("\nA string is not a valid input!\n")
                    continue

                if human < 0:
                    print("\nThe number can't be negative!\n")
                    continue
                elif human > 1000000:
                    print("\nInvalid input! The number can't be bigger than 1000000.\n")
                    continue

                break

            points: int = abs(num - human)
            against: int = abs(num - comp)

            print(f"\nThe robot entered the number {comp}.")
            print(f"The goal number is {num}.")

            if points < against:
                print("You won!")
                wins += 1
            elif points > against:
                print("The robot won!")
                losses += 1
            else:
                print("It's a draw!")
                draw += 1

    def rps(self):

        wins: int = 0
        losses: int = 0
        draw: int = 0

        while True:

            choices: Tuple[str, str, str] = ("rock", "paper", "scissors")

            while True:

                dec: str = input("\nWhat is your move?\n").lower()

                if dec == "exit game":
                    print(f"""
You won: {wins},
The robot won: {losses},
Draws: {draw}.
""")
                    prevb: int = self.boredom
                    prevo: int = self.overheat

                    if self.boredom - 20 >= 0:
                        self.boredom -= 20
                    else:
                        self.boredom = 0
                    if self.overheat + 10 <= 100:
                        self.overheat += 10
                    else:
                        self.overheat = 100
                        print(f"The level of overheat reached 100, {self.name} has blown up!")
                        print("Game over. Try again?")
                        sys.exit()

                    print(f"{self.name}'s level of boredom was {prevb}. Now it is {self.boredom}.")
                    print(f"{self.name}'s level of overheat was {prevo}. Now it is {self.overheat}.")

                    if self.boredom == 0:
                        print(f"{self.name} is in a great mood!")

                    return

                if dec not in choices:
                    print("No such option! Try again!")
                    continue

                break

            rob_choice: str = random.choice(choices)
            print(f"The robot chose {rob_choice}")

            if rob_choice == dec:
                print("It's a draw!")
                draw += 1

            elif (rob_choice == 'paper' and dec == 'scissors') \
                or (rob_choice == 'scissors' and dec == 'rock') \
                    or (rob_choice == 'rock' and dec == 'paper'):

                print("You won!")
                wins += 1
            else:
                print("The robot won!")
                losses += 1

    @property
    def recharge(self) -> None:
        if self.battery == 100:
            print(f"\n{self.name} is charged!")
        else:
            prevb: int = self.battery
            prevbor: int = self.boredom
            prevo: int = self.overheat

            if self.battery + 10 <= 100:
                self.battery += 10
            else:
                self.battery = 100
            if self.overheat - 5 >= 0:
                self.overheat -= 5
            else:
                self.overheat = 0
            if self.boredom + 5 <= 100:
                self.boredom += 5
            else:
                self.boredom = 100

            print(f"\n{self.name}'s level of overheat was {prevo}. Now it is {self.overheat}.")
            print(f"{self.name}'s level of the battery was {prevb}. Now it is {self.battery}.")
            print(f"{self.name}'s level of boredom was {prevbor}. Now it is {self.boredom}.\n")
            print(f"{self.name} is recharged!")

    @property
    def sleeping_mode(self) -> None:

        if self.overheat == 0:
            print(f"\n{self.name} is cool!")
        else:
            prevo: int = self.overheat
            if self.overheat - 20 >= 0:
                self.overheat -= 20
            else:
                self.overheat = 0

            print(f"\n{self.name}'s level of overheat was {prevo}. Now it is {self.overheat}.")

            if self.overheat == 0:
                print(f"\n{self.name} is cool!")
            else:
                print(f"\n{self.name} cooled off!")

    @property
    def info(self) -> None:
        print(f"""\n{self.name}'s stats are: battery is {self.battery},
overheat is {self.overheat},
skill level is {self.skills},
boredom is {self.boredom}.""")

    @property
    def learn(self) -> None:
        if self.skills == 100:
            print(f"\nThere's nothing for {self.name} to learn!")
        elif self.battery <= 0:
            print(f"\nThe level of battery is {self.battery}, {self.name} needs recharging!")
        else:
            if self.battery <= 10:
                print(f"\nGuess what! {self.name} fell into the pool!")
                prevr: int = self.rust

                if self.rust + 50 <= 100:
                    self.rust += 50
                else:
                    self.rust = 100

                if self.rust >= 100:
                    print(f"\n{self.name} is too rusty! Game over. Try again?")
                    self.exit()

            elif self.battery <= 30:
                print(f"\nOh no, {self.name} stepped into a puddle!")
                prevr = self.rust

                if self.rust + 10 <= 100:
                    self.rust += 10
                else:
                    self.rust = 100

            prevs: int = self.skills
            prevo: int = self.overheat
            prevb: int = self.battery
            prevbor: int = self.boredom

            if self.skills + 10 <= 100:
                self.skills += 10
            else:
                self.skills = 100
            if self.battery - 10 >= 0:
                self.battery -= 10
            else:
                self.battery = 0
            if self.overheat + 10 < 100:
                self.overheat += 10
            else:
                self.overheat = 100
                print(f"\nThe level of overheat reached 100, {self.name} has blown up!")
                print("Game over. Try again?")
                sys.exit()
            if self.boredom + 5 <= 100:
                self.boredom += 5
            else:
                self.boredom = 100

            print(f"\n{self.name}'s level of skill was {prevs}. Now it is {self.skills}.")
            print(f"{self.name}'s level of overheat was {prevo}. Now it is {self.overheat}.")
            print(f"{self.name}'s level of the battery was {prevb}. Now it is {self.battery}.")
            print(f"{self.name}'s level of boredom was {prevbor}. Now it is {self.boredom}.")

            if prevb <= 30:
                print(f"{self.name}'s level of rust was {prevr}. Now it is {self.rust}.")

            print(f"\n{self.name} has become smarter!")

    @property
    def work(self) -> None:
        if self.skills < 50:
            print(f"\n{self.name} has got to learn before working!")
        elif self.battery <= 0:
            print(f"\nThe level of the battery is {self.battery}, {self.name} needs recharging!")
        else:
            if self.battery <= 10:
                print(f"\nGuess what! {self.name} fell into the pool!")
                prevr: int = self.rust

                if self.rust + 50 <= 100:
                    self.rust += 50
                else:
                    self.rust = 100

                if self.rust >= 100:
                    print(f"{self.name} is too rusty! Game over. try again?")
                    sys.exit()

            elif self.battery <= 30:
                print(f"\nOh no, {self.name} stepped into a puddle!")
                prevr = self.rust

                if self.rust + 10 <= 100:
                    self.rust += 10
                else:
                    self.rust = 100

            prevb: int = self.battery
            prevbor: int = self.boredom
            prevo: int = self.overheat

            if self.battery - 10 >= 0:
                self.battery -= 10
            else:
                self.battery = 0
            if self.boredom + 10 <= 100:
                self.boredom += 10
            else:
                self.boredom = 100
            if self.overheat + 10 < 100:
                self.overheat += 10
            else:
                self.overheat = 100
                print(f"\nThe level of overheat reached 100, {self.name} has blown up!")
                print("Game over. Try again?")
                sys.exit()

            print(f"\n{self.name}'s level of boredom was {prevbor}. Now it is {self.boredom}.")
            print(f"{self.name}'s level of overheat was {prevo}. Now it is {self.overheat}.")
            print(f"{self.name}'s level of the battery was {prevb}. Now it is {self.battery}.")

            if prevb <= 30:
                print(f"{self.name}'s level of rust was {prevr}. Now it is {self.rust}.")

            print(f"\n{self.name} did well!")

    @property
    def oil(self):
        if self.rust == 0:
            print(f"\n{self.name} is fine, no need to oil!")
        else:
            prevo: int = self.rust
            if self.rust - 20 >= 0:
                self.rust -= 20
            else:
                self.rust = 0

            print(f"{self.name}'s level of rust was {prevo}. Now it is {self.rust}. {self.name} is less rusty!")

    @staticmethod
    def exit():
        print("\nGame over")
        sys.exit()


rob_name = input("How will you call your robot?\n")

if rob_name:
    robot = Robot(rob_name)
else:
    robot = Robot()

actions = ('exit', 'info', 'recharge', 'sleep', 'play', 'learn', 'oil', 'work')

while True:

    print(f"""
Available interactions with {robot.name}:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills
""")

    choice: str = input("Choose:\n").lower()

    if choice not in actions:
        print("\nInvalid input, try again!")

    elif choice == 'info':
        robot.info
    elif choice == 'sleep':
        robot.sleeping_mode
    elif choice == 'recharge':
        robot.recharge
    elif choice == 'play':
        robot.play()
    elif choice == 'exit':
        robot.exit()
    elif choice == 'learn':
        robot.learn
    elif choice == 'work':
        robot.work
    elif choice == 'oil':
        robot.oil
