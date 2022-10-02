"""Example implementing a list utility function"""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# return type bool
# Gameplan:
# 1. Start with the first index
# 2. Loop through the first index
# 3. A test if item at index equal to meedle
# 4. A true return true! We found it!
3. 
def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i< len(haystack):
        if haystack[i] == needle:
            return True
        i += 1

    return False   

           
