from random import *
import time
from Tiles import *


# from numba import jit

def allPossibleTiles(numBorderValues):
    lst = []
    for i in range(1, numBorderValues + 1):
        for j in range(1, numBorderValues + 1):
            for x in range(1, numBorderValues + 1):
                for y in range(1, numBorderValues + 1):
                    lst.append(Tile(i, j, x, y))
    return lst


def randomTiles(numBorderValues, numTiles):
    lst = []
    while len(lst) < numTiles:
        s1 = Edge([1, ()])
        s2 = Edge([1, ()])
        s3 = Edge([1, ()])
        s4 = Edge([1, ()])

        tile = Tile([s1, s2, s3, s4])
        if tile not in lst:
            lst.append(tile)
    return lst


startTime = time.time()


def main():
    tiles = randomTiles(2, 16)
    for i in range(10):
        tiles[i].showBorders()
        print()
    print()
    g = Graph(10, 10)
    g.gen(tiles, g.random_choose)
    g.display()
    print()
    g.gen(tiles, g.abs_different_choose((1, 1, 1, 1)))
    g.display()
    print()
    g.gen(tiles, g.abs_similar_choose)
    g.display()
    print()
    g.gen(tiles, g.signed_different_choose)
    g.display()
    print()
    g.gen(tiles, g.signed_similar_choose)
    print("\n")


main()
print(time.time() - startTime)
