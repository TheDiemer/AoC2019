#!/bin/python3
import sys
from os import path
from math import floor


def fuel(weight):
    total = 0
    fuelReq = floor(weight / 3)
    while True:
        if fuelReq <= 0:
            break
        else:
            fuelReq = fuelReq - 2
            if fuelReq <= 0:
                break
            else:
                total += fuelReq
        fuelReq = floor(fuelReq / 3)
    return total


def main(moduleWeight):
    with open(moduleWeight) as opened:
        line = opened.readline()
        total = 0
        while line:
            print("Got {0}".format(int(line)))
            req = fuel(int(line))
            total += req
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
