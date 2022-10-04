
"""My barracks for testing functions"""
_author_ = "730495262"

def only_evens(xs: list[int]) -> list[int]:
    #function that returns the even values in a list of integers
    ys: list[int]= list()
    for number in xs:
        if number % 2 == 0:
            ys.append(number)
    print(ys)
    return ys

def concat(xs: list[int], ys: list[int]) -> list[int]:
    # function that combines (concatenates) two lists of integers together
    zs: list[int] = list()
    for number in xs:
        zs.append(number)
   
    for number in ys:
        zs.append(number)
    print(zs)
    return zs

def sub(start: int, end: int, xs: list[int]) -> list[int]:
    #a List which is a subset of the given list
    # between the specified start index and the end index - 1
    ys: list[int]=list()
    if len(xs) == 0 or start > len(xs)-1 or end <= 0:
        return ys
    if start < 0:
        counter=0
    else:
        counter = start
    if end > len(xs):
        end = len(xs)

    while counter < end:
        ys.append(xs[counter])
        counter+=1
        
    return ys