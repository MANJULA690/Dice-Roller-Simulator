import random
import time

def roll_dice():
    print("Rolling the dice", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    result = random.randint(1, 6)
    print(f"\n🎲 You rolled a {result}!\n")


print("🎲 Welcome to Dice Roller Simulator!")
input("Press Enter to roll the dice...")

roll_dice()
