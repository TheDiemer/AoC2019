#!/bin/python3
import sys
from os import path
from math import floor


def main(lower, upper):
    # This will track the number of passwords that meet the criteria
    answer = 0
    # We will use this to shrink our options down from lower-upper down to a list of numbers that only increase (or remain the same) from left to right
    increasing = []
    # Start by looping over All of the numbers in out range!
    for number in range(lower, upper + 1):
        # Set this to 0 so we track the position in the 6 digit number
        place = 0
        # Set the array to empty so it starts that way for each number
        increase = []
        # Loop over each digit in the number
        for part in str(number):
            # So long as we are not looking at the first digit
            if place > 0:
                # check if the current digit is greater than or equal to the digit immediately before it
                if int(part) >= int(str(number)[place - 1]):
                    # If it is then add True to the list
                    increase.append(True)
                # otherwise add False to the list
                else:
                    increase.append(False)
            # Move the location of the counter forward to make it easier to track the spot
            place += 1
        # If ALL of the digits are equal to or greater than the ones before it, then add it to our new list
        if False not in increase:
            increasing.append(number)

    # Now to loop over our NEW set of numbers
    for number in increasing:
        # Set double to False so that each number is assumed (until proven otherwise) to NOT have a double in it
        double = []
        # Set this to 0 so we track the position in the 6 digit number
        place = 0
        # Loop over each digit in the number
        for part in str(number):
            # So long as we are not looking at the first digit
            if place == 1:
                # check if the current digit is the same as the digit right before it
                if int(part) == int(str(number)[place - 1]):
                    # If it is, flip our flag to True!
                    double.append(True)
            # Check starting two places forward
            elif place > 1:
                if int(part) == int(str(number)[place - 1]) and int(part) != int(
                    str(number)[place - 2]
                ):
                    double.append(True)
                # If it is equal to two digits before AND 1 digit before
                elif int(part) == int(str(number)[place - 2]) and int(part) == int(
                    str(number)[place - 1]
                ):
                    # reset it to false
                    double.pop()
                    double.append(False)
            # Move the location of the counter forward to make it easier to track the spot
            place += 1
        # If the double flag is true, increase our answer counter!
        if True in double:
            answer += 1
    print(
        "In the range of {0}-{1}, there are {2} possible passwords that meet the criteria".format(
            lower, upper, answer
        )
    )


if __name__ == "__main__":
    inpt = "265275-781584"
    lower = int(inpt.split("-")[0])
    upper = int(inpt.split("-")[1])
    main(lower, upper)
