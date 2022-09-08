#!/usr/bin/python

"""
Python Core object Types
"""

def number():
    """
       This is to review numbers and basic operations.
       """
    # Write the value 4 to the power of 5 and assign it to variable x
    x =
    # Write the value x divided by 3 and assign it to variable y
    y =
    return x,y
def strings():
    """
    This is to review numbers and strings and basic operations.
    """

    # Assign a string "stevens" to a variable stevens.

    stevens =

    # Repeat variable stevens 7 times and assign it to variable stevens_7.

    stevens_7 =

    # What is the length of stevens_7?

    length =

    # Concatenate variable stevens with string " is great" and assign it to variable great.

    great =

    # Replace "great" with "good" in variable m and assign it to a new variable good.

    good =

    return stevens, stevens_7, length, great, good


def list_1D():
    """
    This is to review basic operations with lists.
    """
    s = "\nhoboken,is,awesome,i,like,it\n"
    #Remove whitespace characters on both side and assign it to a new variable.

    hoboken =

    # Split variable n on a delimiter space into a list of substrings and assign it to a new variable hoboken_list.

    hoboken_list =

    # Get the first item in the hoboken_list and assign it to a new variable hoboken_first_item.

    hoboken_first_item =

    ####
    l=[2,3,4,1,5,6,9,10,15,12,13,-2,-6,0,0]

    # Sort list l (make sure you use inplace sort).


    # Get the 4th to 10th item in sorted list l and assign them to a new list new_l.

    new_l =

    return hoboken,hoboken_list, hoboken_first_item, l, new_l

def list_2D():
    # Create a 3 x 3 matrix A as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]

    A =

    # Collect the items in the last column of matrix A using list comprehension and assign it to a new variable last_column.

    last_column =

    # Get the item at the last row and last column of A.

    a =

    # Get the item at row 2 and column 1 of A.

    b =


    return A,last_column, a, b


def dictionary():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   "fruit" => "apple"
    #   "quantity" => 18
    #   "color" => "red"
    fruit_dict =

    # Get the item in dictionary fruit_dict that the key "fruit" maps to.

    f =

    # Increase the quantity of f by 1


    return fruit_dict, f
def dictionary_nested():
    # Create a nested dictionary Grace where:
    #   "name" => {"first_name" => "Grace", "last_name" => "Hopper"} (a dictionary)
    #   "jobs" => ["scientist", "engineer"] (a list)
    #   "age" => 85

    Grace =

    # Get the "last_name" from "name".

    last_name =

    # Add "programmer" to the list of "jobs" Grace has.



    # Get the third job Grace has that you recently added.

    job =


    return Grace,last_name, job



