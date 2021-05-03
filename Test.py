from Graph import *
from Tile import *
from random import *
from Level import *
from Tileset import *
import time
import json


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
        tile = Tile(randrange(1, numBorderValues + 1), randrange(1, numBorderValues + 1),
                    randrange(1, numBorderValues + 1), randrange(1, numBorderValues + 1))
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
    tiles = randomTiles(4, 4 ** 4)
    # for i in tiles:
    # i.showBorders()
    # print()
    # tiles2 = allPossibleTiles(4)
    # tiles3 = [i for i in tiles if i in tiles2]
    # print(len(tiles), len(tiles2), len(tiles3))
    # print()
    """g = Graph(10, 10)
    print("Random Graph")
    g.gen(tiles, g.random_choose)
    g.display()
    print()
    print("Abs-Diff Graph")
    g.gen(tiles, g.abs_different_choose)
    g.display()
    print()
    print("Abs-Sim Graph")
    g.gen(tiles, g.abs_similar_choose)
    g.display()
    print()
    print("Sig-Diff Graph")
    g.gen(tiles, g.signed_different_choose)
    g.display()
    print()
    print("Sig-Sim Graph")
    g.gen(tiles, g.signed_similar_choose)
    g.display()
    print("\n")
    # print(json.dumps(g))"""

    l = Level(tiles, 10, 10, None, None, None, None)
    l.update_function(Graph.random_choose)
    l.re_gen()
    print("Random")
    l.tiling.display()
    print()
    l.update_function(Graph.abs_different_choose)
    l.re_gen()
    print("Abs Diff")
    l.tiling.display()
    print()
    l.update_function(Graph.abs_similar_choose)
    l.re_gen()
    print("Abs Sim")
    l.tiling.display()
    print()
    l.update_function(Graph.signed_different_choose)
    l.re_gen()
    print("Sig Diff")
    l.tiling.display()
    print()
    l.update_function(Graph.signed_similar_choose)
    l.re_gen()
    print("Sig Sim")
    l.tiling.display()
    print()


main()
print(time.time() - startTime)
