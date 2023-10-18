# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: ar
"""
import datetime


def my_brand():
    """
    function for my brand that returns the date and the assignment
    """
    assignment = "HW-2"
    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(
        "=*=*=*= Ashna Razdan =*=*=*=\n=*=*=*= Course 2023S-SSW567 =*=*=*=\n=*=*=* "
        + assignment
        + " =*=*=*=\n =*=*=*= "
        + date
        + " =*=*=*="
    )


def classify_invalid(a, b, c):
    """
    Classifies if a triangle is invalid
    """
    invalid = False
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        invalid = True

    if a <= 0 or b <= 0 or c <= 0:
        invalid = True

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        invalid = True

    return invalid


def classify_triangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    if classify_invalid(a, b, c) is True:
        return "InvalidInput"

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return "NotATriangle"

    # now we know that we have a valid triangle
    if a == b and b == c and c == a:
        return "Equilateral"
    if (
        (a**2 + b**2 == c**2)
        or (c**2 + b**2 == a**2)
        or (a**2 + c**c == b**2)
    ):
        return "Right"
    if (a == b) or (b == c) or (c == a):
        return "Isoceles"
    return "Scalene"
