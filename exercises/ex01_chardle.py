"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730495262"

contains: bool = False

question: str = input("Enter a 5-character word: ")
if len(question) != 5:
    print("Error: Word Must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + question)

counter: int = 0
if letter == question[0]:
    print(letter + " found at index 0")
    counter+=1
    contains = True
if letter == question[1]:
    print(letter + " found at index 1")
    counter+=1
    contains = True
if letter == question[2]:
    print(letter + " found at index 2")
    counter+=1
    contains = True
if letter == question[3]:
    print(letter + " found at index 3")
    counter+=1
    contains = True
if letter == question[4]:
    print(letter + " found at index 4")
    counter+=1
    contains = True
elif contains is False:
    print("No instances of " + letter + " found in " + question)
    exit()
if counter == 1:
    print(str(object=counter) + " instance of " + letter + " found in " + question)
else:
    print(str(object=counter) + " instances of " + letter + " found in " + question)