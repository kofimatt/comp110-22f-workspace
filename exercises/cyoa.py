"""Some kind of mystery that involves searching a sequence of rooms."""
_author_ = "730495262"



from random import randint


points: int = 0
player: str = str(object=input("NPC: Detective, what is your name! We've been waiting for you🙀."))
# I tried to assign the player variable to globals in my greet procedure but it didn't work and I couldn't figure out why😫. Please spare me!!!!!!!
# Following three variables are the clues that will be displayed if room one is the room that contains the clue to the killer
clue_one_room_one: str = "Blood soaked garments laid across the floor"
clue_two_room_one: str = "Butcher knife next to notes on how to slice the fatty parts out of flesh"
clue_three_room_one: str = "Potato plant🥔"
# ---------------------
# Following three variables are the clues that will be displayed if room two is the room that contains the clue to the killer
clue_one_room_two: str = "Television turned to 'Jeffery Dahmer: a serial killer's documentary"
clue_two_room_two: str = "Application to be a computer science major"
clue_three_room_two: str = "5 different sized gloves"
# ---------------------
# Following three variables are the clues that will be displayed if room three is the room that contains the clue to the killer
clue_one_room_three: str = "Invitation to KillersRUs"
clue_two_room_three: str = "Loaded gun🔫"
clue_three_room_three: str = "10 copies of Shrek 2"
"""The clue choice variable will be set to the clue that the person chooses"""
user_clue_input: int = 0
def greet()-> None:
    # This "greet" procedure will be called to greet the player and is called at the beginning of the "main" procedure
    print("NPC: Oh how we've been waiting for you.")
    print("NPC: There has been a murder and we need you to search rooms and check the room for clues")
    print("Game: There are three rooms and three clues per room. One clue in each room will lead to catching the killer.")
    print("If all three clues are collected, you win the game!")


def game_over()-> None:
    # "Gameover" serves the purpose of ending the game and will be called when a certain condition is met
    print()
    print(f"{player} thankyou for playing. You finished with {points} points")
    print("Unfortunately you could not identify the killer🥲")
    play_again: str = input("Would you like to play again? Reply with Y or N.")
    if play_again == "Y":
        main()
    else:
        print("goodbye😫")
    

def room(x: int)-> None:
    # function that in tandem with the while loop in the main procedure, will cycle through the rooms and display the clues
    if x == 1:
        print()
        print("Welcome to room 1. Here are the clues:") 
        print(clue_one_room_one)
        print(clue_two_room_one) 
        print(clue_three_room_one) 
    elif x == 2:
        print()
        print("Welcome to rooom 2. Here are the clues:")
        print(clue_one_room_two)
        print(clue_two_room_two)
        print(clue_three_room_two)
    elif x == 3:
        print()
        print("Welcome to room 3. Here are the clues:")
        print(clue_one_room_three)
        print(clue_two_room_three)
        print(clue_three_room_three)
   



def clue_input()-> int:
    # Function that when called, asks the user what clue they would like to use
    global user_clue_input
    user_clue_input = int(input("What clue would you like to choose. Type '1' for clue 1, '2' for clue 2, or '3' for clue 3." ), base=10)
    return user_clue_input

def clue_choice(x: int)->None:
    global points
    correct_clue: int = randint(1,3)
    if x == correct_clue:
        points+=5
        print()
        print("You chose the correct clue")
        print(f"{player} you now have {points} points‼️")
    else:
        print()
        print("Game: Wrong clue picked.")

def game_won()-> None:
    print()
    print("You have found the killer with your great detective intuition. Thankyou!")
    print(f"{player}, you have finished with 15 points❤️‍🔥")

def main()-> None:
    global points
    global user_clue_input
    global player
    i: int = 1
    greet()
    ready_to_play: str = str(object=input("Are you ready to play? Reply with 'Y' for yes or 'N' for no" ))
    if ready_to_play == "Y":
        print()
    else:
        game_over()
    while i<=3:
        room(i)
        clue_choice(clue_input())
        i+=1
    if points == 15:
        game_won()
    else:
        game_over()

if __name__ == "__main__":
    main()

    