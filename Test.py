from Graph import *
from Tile import *
from random import *
import time
from numba import jit

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
    while len(lst)<numTiles:
        tile = Tile(randrange(1,numBorderValues+1), randrange(1,numBorderValues+1),randrange(1,numBorderValues+1),randrange(1,numBorderValues+1))
        if tile not in lst:
            lst.append(tile)
    return lst
#
# for i in randomTiles(4, 20):
#     i.showBorders()
# tiles = [Tile(1, 1, 1, 1), Tile(1, 1, 1, 2), Tile(1, 1, 2, 1), Tile(1, 1, 2, 2), Tile(1, 2, 1, 1), Tile(1, 2, 1, 2),
#          Tile(1, 2, 2, 1), Tile(1, 2, 2, 2), Tile(2, 1, 1, 1), Tile(2, 1, 1, 2), Tile(2, 1, 2, 1), Tile(2, 1, 2, 2),
#          Tile(2, 2, 1, 1), Tile(2, 2, 1, 2), Tile(2, 2, 2, 1)]
#
startTime = time.time()

def main():
    tiles = randomTiles(20,(20**4)/4)
    g = Graph(10, 10)
    g.gen(tiles)
    print("\n")
    g.display()

main()
print(time.time() - startTime)