#!/bin/python3
import sys
from os import path
from math import floor


def cal(programList):
    place = 0
    while place <= len(programList):
        operation = int(programList[place])
        if operation == 99:
            break
        else:
            firstLocation = int(programList[place + 1])
            secondLocation = int(programList[place + 2])
            storageLocation = int(programList[place + 3])
            if operation == 1:
                calculation = int(programList[firstLocation]) + int(
                    programList[secondLocation]
                )
            elif operation == 2:
                calculation = int(programList[firstLocation]) * int(
                    programList[secondLocation]
                )
            else:
                calculation = programList[storageLocation]

            programList[storageLocation] = calculation

        # move forward 4 places
        place += 4
    return programList


def main(filePath):
    with open(filePath) as opened:
        program = opened.readline()
    programList = program.split(",")
    for noun in range(100):
        for verb in range(100):
            programList = program.split(",")
            programList[1] = str(noun)
            programList[2] = str(verb)
            response = cal(programList)
            if int(response[0]) == 19690720:
                print((100 * int(response[1])) + int(response[2]))
                return (100 * int(response[1])) + int(response[2])


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
