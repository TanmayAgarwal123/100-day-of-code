#path: 100%20Days%20100%20Projects/Day%203%20tresure%20hunt/main.py
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

import time

def game_intro():
    print("Welcome to the Mysterious Island Treasure Hunt!")
    print("You find yourself on a deserted island. Your goal is to find the hidden treasure.")
    print("Be careful; the island is full of mysteries and dangers.")
    input("Press Enter to start your adventure...")
    clear_screen()

def lost_game():
    clear_screen()
    print("You lost the game. Better luck next time!")
    print("Thanks for playing.")

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_path(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice. Try again.")

def forest_stage():
    clear_screen()
    print("You enter a dense forest. The path splits into three:")
    
    choice = choose_path("Which path will you choose?", ["Left", "Center", "Right"])
    if choice == 1:
        print("You chose the left path and encounter a pack of wolves.")
        time.sleep(2)
        lost_game()
    elif choice == 2:
        print("You chose the center path and find an old map. It leads you deeper into the forest.")
        time.sleep(2)
        forest_stage()
    else:
        print("You chose the right path and discover a hidden cave entrance.")
        time.sleep(2)
        cave_stage()

def cave_stage():
    clear_screen()
    print("You explore the dark cave. There are two passages:")
    choice = choose_path("Which passage will you take?", ["Narrow Passage", "Glowing Mushrooms"])

    if choice == 1:
        print("You squeeze through the narrow passage and find a hidden chamber.")
        time.sleep(2)
        treasure_chest_stage()
    else:
        print("You follow the path with glowing mushrooms. They light the way deeper into the cave.")
        time.sleep(2)
        underground_river_stage()

def treasure_chest_stage():
    clear_screen()
    print("You find a massive treasure chest!")
    print("To unlock the chest, you must solve a riddle:")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer == "an echo":
            print("Correct! The treasure chest opens, revealing precious jewels and gold.")
            time.sleep(2)
            win_game()
            break
        else:
            print("Incorrect. Try again.")

def underground_river_stage():
    clear_screen()
    print("You arrive at an underground river. There is a boat waiting for you.")
    
    choice = choose_path("Will you take the boat or continue on foot?", ["Take the boat", "Continue on foot"])
    
    if choice == 1:
        print("You take the boat and sail through the underground river. The boat leads you to a hidden cavern.")
        time.sleep(2)
        ancient_temple_stage()
    else:
        print("You continue on foot and come across a treacherous bridge over the river.")
        time.sleep(2)
        bridge_collapse_stage()

def ancient_temple_stage():
    clear_screen()
    print("You discover an ancient temple with three doorways:")
    
    choice = choose_path("Which doorway will you choose?", ["Left", "Center", "Right"])
    
    if choice == 1:
        print("You enter the left doorway and find yourself in a room filled with ancient artifacts.")
        time.sleep(2)
        win_game()
    elif choice == 2:
        print("You enter the center doorway and encounter a booby trap.")
        time.sleep(2)
        lost_game()
    else:
        print("You enter the right doorway and are met with a dark corridor.")
        time.sleep(2)
        dark_corridor_stage()

def dark_corridor_stage():
    clear_screen()
    print("You navigate the dark corridor. Suddenly, you hear growling and see glowing eyes in the distance.")
    
    choice = choose_path("Do you run or try to hide?", ["Run", "Hide"])
    
    if choice == 1:
        print("You run as fast as you can and escape the danger.")
        time.sleep(2)
    else:
        print("You hide in a small alcove and the danger passes by.")
        time.sleep(2)
    
    print("After a while, you find a staircase leading up.")
    time.sleep(2)
    rooftop_stage()

def rooftop_stage():
    clear_screen()
    print("You climb the staircase and emerge onto the rooftop of the ancient temple.")
    print("In the distance, you see the glittering treasure.")
    
    choice = choose_path("How will you reach the treasure?", ["Use a grappling hook", "Climb down and take the stairs"])
    
    if choice == 1:
        print("You use the grappling hook to reach the treasure. Success!")
        time.sleep(2)
        win_game()
    else:
        print("You climb down and take the stairs, reaching the treasure safely.")
        time.sleep(2)
        win_game()

def bridge_collapse_stage():
    clear_screen()
    print("You attempt to cross the treacherous bridge over the underground river.")
    print("Suddenly, the bridge collapses!")

    choice = choose_path("What will you do?", ["Swim to safety", "Hold onto debris"])
    
    if choice == 1:
        print("You swim to safety and reach the other side of the river.")
        time.sleep(2)
    else:
        print("You hold onto debris and wait for help.")
        time.sleep(2)
    
    print("After a while, you find another path.")
    time.sleep(2)
    ancient_temple_stage()

def win_game():
    clear_screen()
    print("Congratulations! You've found the hidden treasure and won the game.")
    print("You are now the richest person on the island!")

def main():
    game_intro()
    forest_stage()

if __name__ == "__main__":
    main()

