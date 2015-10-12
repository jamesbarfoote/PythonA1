#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
# James Barfoote
# ID: 300279899
import math

"""
This module contains the functions that relate to the first three
lectures of the course (basic training and lists). 
"""

# _if_name_ == "_main_";

def distance(t, accel):
    """Print the distance travelled.

    Calculates the distance travelling in a given time (t) at a given
    acceleration (accel).

    You should round the result to ONE decimal places (use the round
    method, for example round(10.01,1) creates the output 10.0). Why
    do this? To hide any problems related to floating point precision.

    Args:
       t is an integer
       accel is a float

       Import the functions
>>> from assignment1 import distance

Test the distance calculation
>>> for t in range(0,10):
...     distance(t,9.8)
...
0.0
4.9
19.6
44.1
78.4
122.5
176.4
240.1
313.6
396.9


    """
    if accel == 0 and t == 0:
        print("No accelleration or time")


    dist = (round(0.5*accel * t ** 2,1))
    print(dist)


def pythagoras(a, b):
    """Find the length of a third side of a triangle.

    Uses pythagoras' theorem to calculate the length, that is the sum
    of the squares of two legs (a and b) is equal to the sum of the
    squares of the other leg.

    If a and b are both equal or greater than zero, print
    the length of the leg.

    If a is zero or negative print "First leg is invalid"

    If b is zero or negative print "Second leg is invalid"

    Again you should round the output to one decimal place (hide
    precision problems).

    Args:
       a is an integer or float
       b is an integer or float

       Import the functions
>>> from assignment1 import pythagoras

Test the pythagoras code
>>> pythagoras(3,4)
5.0
>>> pythagoras(4,3)
5.0
>>> pythagoras(0,3)
First leg is invalid
>>> pythagoras(3,0)
Second leg is invalid
>>> pythagoras(3,3)
4.2
>>>

    """
    if a == 0 or a < 0:
        print("First leg is invalid")

    if b == 0 or b < 0:
        print("Second leg is invalid")

    if a == b or (a > 0 and b > 0):
        print(round(math.sqrt((a ** 2) + (b ** 2)),1))


def grade(mark, mcr):
    """Assign a letter grade based on a mark

    Implement this grading scheme.

    A between 80 and 100
    B between 65 and 79
    C between 50 and 64
    D between 40 and 49
    E between 0 and 39

    K Fail due to not satisfying mandatory course requirements, even
      though the student’s numerical course mark reached the level
      specified for a pass, usually 50%. A student whose course mark
      is below 50 should be given a D (40–49) or E (0 –39), regardless
      of whether they met the mandatory course requirements.

    You should sanity check the types of the inputs.

    Args: 
       mark is an integer mark, if not integer print "Invalid mark"

       mcr is a boolean (True if met mandatory requirements, False
        if have not met them), if not boolean print "Invalid mcr"

        import the functions
>>> from assignment1 import grade

Test the grading code
>>> grade(0, True)
E
>>> grade(40, True)
D
>>> grade(45, True)
D
>>> grade(50, True)
C
>>> grade(55, True)
C
>>> grade(55, False)
K
>>> grade(66, True)
B
>>> grade(66, False)
K
>>> grade(76, False)
K
>>> grade(76, True)
B
>>> grade(86, True)
A
>>> grade(86, False)
K
>>> grade(0.0,True)
Invalid mark
>>> grade(0.0,False)
Invalid mark
>>> grade(0,"dsafdsfd")
Invalid mcr

    """
    if not isinstance(mark, int):
        print("Invalid mark")
    else:
        if not isinstance(mcr, bool):
            print("Invalid mcr")
        else:
            if mcr == False:
                print("K")
            else:
                if mcr == True and mark >= 80 and mark <= 100:
                    print("A")
                else:
                    if mcr == True and mark <= 79 and mark >= 65:
                        print("B")
                    else:
                        if mcr == True and mark <= 64 and mark >= 50:
                                print("C")
                        else:
                                if mcr == True and mark <= 49 and mark >= 40:
                                    print("D")
                                else:
                                    if mcr == True and mark <= 39 and mark >= 0:
                                        print("E")




def print_before(text, marker):
    """Count how many words occur in a given piece of text up to a marker 

    Given a piece of text and a given marker word, display all the
    words from the beginning of the text through to (and including the
    marker word).

    Print the entire list of words in the text should the marker not
    be found (use list operators to implement this functionality).
     
    You should check the arguments and print an error message if the
    types of the argument are different from expected.

    For example, if the text is not a list display "Expected a list of
    words" and if the marker is not string display "Expected a string".

    Args:
      text is a list of words
      marker is a string

      Import the functions
>>> from assignment1 import print_before

Test the list problem:
>>> print_before(["a","b","c"],"b")
['a']
>>> print_before(["a","b","c"],"c")
['a', 'b']
>>> print_before(["a","b","c"],"")
['a', 'b', 'c']
>>> print_before([],"")
[]
>>> print_before([],"a")
[]
>>> print_before([],[])
Expected a string
>>> print_before([],"a")
[]
>>> print_before("","a")
Expected a list of words

    """

    l = []

    if marker == [] and text == []:
        print("Expected a string")
        return

    else:
        if text == "" and marker == "":
            print("Expected a list of words")
            return

    for word in text:

        if word == marker:
            break
        l.append(word)

    print(l)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


