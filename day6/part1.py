#!/bin/python3
import sys
from os import path
from math import floor


def main(orbitList):
    oMap = {}
    with open(orbitList) as opened:
        line = opened.readline()
        while line:
            parts = line.split(")")
            if len(oMap) > 0:
                if parts[0] in oMap:
                        tmp = oMap[parts[0]]
                        tmp.append(parts[1].rstrip())
                        oMap[parts[0]] = tmp
                else:
                    oMap[parts[0]] = [parts[1].rstrip()]
            else:
                oMap[parts[0]] = [parts[1].rstrip()]
            line = opened.readline()
    print(oMap)
    orbits = 0
    for link in oMap:
        for b in oMap:
            if link in oMap[b]:
                print('{0} is in {1} which is the array for {2}'.format(link, oMap[b], b))



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
