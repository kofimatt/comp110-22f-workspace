"""Exercise 2: One shot Wordle"""
__author__ = "730595262"



secret_word: str = "python"
word_length: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
result: str = ""
guess: str = input(f"What is your {word_length}-letter guess? ")
play: bool = False
exists: bool = False
count: int = 0

while play == False:
    if len(guess) != word_length:
        guess = input(f"That was not {word_length} letters! Try again: ")
    else:
        play = True

while i < len(guess):
    if guess[i] == secret_word[i]:
        result += GREEN_BOX
    else:
        while exists != True and count<len(guess):
            if guess[i] == secret_word[count]:
                exists = True
            else:
                count+=1
        if exists == True:
            result+= YELLOW_BOX
        else:
            result+= WHITE_BOX
    i+=1
    exists = False
    count = 0
print(result)


    




    
    

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    