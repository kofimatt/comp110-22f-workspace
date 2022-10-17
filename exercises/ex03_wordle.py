"""Exercise 3- Structured Wordle."""
__author__ = "730495262"

def contains_char(word_input: str, char: str)-> bool:
    """Determines whether second parameter "char" exists in first parameter "word_input". """
    assert len(char) == 1
    contains: bool = False
    i: int = 0
    while i<len(word_input):
        if word_input[i] == char:
            contains = True
        i+=1
    return contains

def emojified(guess: str, secret: str)-> str:
    """Returns a string of Green, White, and Yellow boxes which is determined by if each letter in guess either match the letter of the same index in secret or if the letter in guess is located somewhere in secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""

    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                result+= YELLOW_BOX
            else:
                result+= WHITE_BOX
        i+=1
    return result

def input_guess(word_length: int)-> str:
    """Returns the user's guess as long as it is the same length as the parameter specifies."""
    guess: str = input(f"Enter a {word_length} character word: ")
    play: bool = False
    while play is False:
        if len(guess) != word_length:
            guess = input(f"That wasn't {word_length} chars! Try again: ")
        else:
            play = True
    return guess

def main()-> None:
    """The Entry point of the program and main game loop."""
    secret_word: str = "codes"
    turn_number = 1
    playing: bool = True
    game_result: str = ""
    while turn_number<7 and playing is True:
        print(f"=== Turn {turn_number}/6 ===")
        user_input: str = input_guess(len(secret_word))
        print(emojified(user_input, secret_word))
        if user_input == secret_word:
            # print(f"You won in {turn_number}/6 turns!")
            game_result = "W"
            playing = False
        
        turn_number +=1
    if game_result == "W":
        print(f"You won in {turn_number-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow")
    
if __name__ == "__main__":
    main()

       

            


