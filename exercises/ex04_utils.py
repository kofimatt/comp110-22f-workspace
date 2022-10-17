"""Exercise 4- 'list' Utility Functions"""
__author__ = "730495262"

def all(xs: list[int], x: int)-> bool:
    """Returns true false based on whether all the integers in the list are the same as the called integet in the parameter"""
    i: int = 0
    condition: bool = True
    while i<len(xs):
        if xs[i] == x:
            condition = True
        else:
            condition = False
            return(condition)
        i+=1
    return condition

def max(xs: list[int])-> int:
    """Returns the largest value in a list of integers"""
    i: int = 1
    largest: int = xs[0]
    if len(xs) == 0:
        raise ValueError("max() arg is an empty list")
    while i<len(xs):
        if largest < xs[i]:
            largest = xs[i]
        i+=1
    return largest

def is_equal(xs: list[int], ys: list[int])-> bool:
    """Returns true if all values in the lists are equal, false if not"""
    i: int = 0
    condition: bool = True
    while i<len(xs):
        if xs[i] != ys[i]:
            condition = False
        i+=1
    return condition
            



