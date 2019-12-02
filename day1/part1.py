#!/bin/python3
import sys
from os import path
from math import floor


def main(moduleWeight):
    with open(moduleWeight) as opened:
        line = opened.readline()
        total = 0
        while line:
            print("Got {0}".format(line))
            num = floor(int(line) / 3) - 2
            print("  the fuel required for that is {0}!".format(num))
            total += num
            line = opened.readline()
    print("\nAll done! The Final total fuel requirements are {0}!".format(total))
    return total


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filePath = sys.argv[1]
        if not path.isfile(path.expanduser(filePath)):
            print(
                "This ({0}) is not a valid file Path! Please put the input file in place and try again!".format(
                    filePath
                )
            )
        else:
            main(path.expanduser(filePath))
    else:
        print("Nope, just provide a file path")
