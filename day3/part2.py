#!/bin/python3
import sys
from os import path
from math import floor


def main(moduleWeight):
    with open(moduleWeight) as opened:

        def crawl():
            location = [0, 0]
            steps = 0
            for move in opened.readline().split(","):
                delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1),}[move[0]]

                for _ in range(int(move[1:])):
                    location[delta[0]] += delta[1]
                    steps += 1
                    yield tuple(location), steps

        visited = {}
        for location, steps in crawl():
            if location not in visited:
                visited[location] = steps
        print(min(
            steps + visited[location]
            for location, steps in crawl()
            if location in visited
        ))


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
