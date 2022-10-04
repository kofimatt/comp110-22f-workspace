"""Python exercise 5 'list utility functions' """
_author_ = "730495262"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens()-> None:
    #Testing for a return of even numbers for a list that includes some even numbers
    xs: list[int]= [2,6,8,9,7]
    assert only_evens(xs) == [2,6,8]

def test_only_evens()-> None:
    #Testing that list of odd numbers returns an empty list
    xs: list[int]= [5, 7, 11]
    assert only_evens(xs) == []

def test_only_evens()-> None:
    #Testing that a list of all even numbers is copied
    xs: list[int]= [2, 2, 2]
    assert only_evens(xs) == [2, 2, 2]
#--------------------------------------------------------------------
"""For concat"""
def test_concat()-> None:
    xs: list[int]= [1,2,3,4]
    ys: list[int]= [5,6,7,8]
    assert concat(xs, ys) == [1,2,3,4,5,6,7,8]

def test_concat()-> None:
    xs: list[int]= []
    ys: list[int]= [5,6,7]
    assert concat(xs, ys) == [5, 6, 7]

def test_concat()-> None:
    xs: list[int]= [4, 8, 6, 3]
    ys: list[int]= [1, 1, 1, 1]
    assert concat(xs, ys) == [4, 8, 6, 3, 1, 1, 1, 1]
#-----------------------------------------------------------------------
def test_sub()-> None:
    xs: list[int] = [1,2,3,4,5,6]
    assert sub(2, 4, xs) == [3,4]

def test_sub()-> None:
    #Testing for if the start index is less than 0
    xs: list[int] = [1,2,3,4,5,6]
    assert sub(-1, 4, xs) == [1, 2, 3, 4]

def test_sub()-> None:
    #Testing for if the end index is greater than the length of the list
    xs: list[int] = [1,2,3,4,5,6]
    assert sub(2, 10, xs) == [3, 4, 5, 6]

def test_sub()-> None:
    #Testing for an empty list argument, start index > length of list, and end index as 0 or lower
    xs: list[int] = []
    assert sub(2, -1, xs) == []

