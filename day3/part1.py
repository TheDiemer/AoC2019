#!/bin/python3
import sys
from os import path
from math import floor


# Credit where credit is due. I did not figure out this logic on my own.
# I learned from the code shared by https://www.reddit.com/user/jadenPete/ in the subreddit
def main(moduleWeight):
    with open(moduleWeight) as opened:

        def crawl():
            location = [0, 0]
            for move in opened.readline().split(","):
                delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1),}[move[0]]

                for _ in range(int(move[1:])):
                    location[delta[0]] += delta[1]
                    yield tuple(location)

        visited = set(crawl())
        closest = min(
            abs(location[0]) + abs(location[1])
            for location in crawl()
            if location in visited
        )
        print(closest)


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
