#!/bin/python3
import sys
from os import path
from math import floor


def main(filePath):
    with open(filePath) as opened:
        program = opened.readline()
    programList = program.split(",")
    place = 0
    while place <= len(programList):
        start = str(programList[place])
        if len(start) >1:
            # Get just the op code out
            operation = int(start[len(start) - 2:])
            # Then get the parameters for the op code
            opParam = start[:len(start) - 2]
            # Put them in the order we care about
            opParam = opParam[::-1]
            if len(opParam) < 3:
                opParam += "0"
        else:
            operation = int(start)
            opParam = "000"
        if operation == 99:
            break
        else:
            if operation in [1, 2, 7, 8]:
                if int(opParam[0]) == 0:
                    first = int(programList[int(programList[place + 1])])
                else:
                    first = int(programList[place + 1])

                if int(opParam[1]) == 0:
                    second = int(programList[int(programList[place + 2])])
                else:
                    second = int(programList[place + 2])
                storageLocation = int(programList[place + 3])
                if operation == 1:
                    calculation = first + second
                elif operation == 2:
                    calculation = first * second
                elif operation == 7:
                    if first < second:
                        calculation = 1
                    else:
                        calculation = 0
                elif operation == 8:
                    if first == second:
                        calculation = 1
                    else:
                        calculation = 0
                else:
                    pass
                # Move place past the 3 parameters
                place += 4
            elif operation in [3, 4]:
                if operation == 3:
                    storageLocation = int(programList[place + 1])
                    calculation = input("temp to get the data:  ")
                elif operation == 4:
                    storageLocation = int(programList[place + 1])
                    calculation = programList[storageLocation]
                    print("{0} was stored at {1}".format(calculation, storageLocation))
                else:
                    pass
                # Move place past the single parameter
                place += 2
            elif operation in [5, 6]:
                if int(opParam[0]) == 0:
                    first = int(programList[int(programList[place + 1])])
                else:
                    first = int(programList[place + 1])
                if int(opParam[1]) == 0:
                    second = int(programList[int(programList[place + 2])])
                else:
                    second = int(programList[place + 2])
                # This is so I dont actually Change any values while not impacting the rest of the logic
                storageLocation = 0
                calculation = programList[storageLocation]
                if operation == 5:
                    if first != 0:
                        place = second
                    else:
                        place += 3
                elif operation == 6:
                    if first == 0:
                        place = second
                    else:
                        place += 3
                else:
                    pass
            else:
                pass

            programList[storageLocation] = calculation


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
