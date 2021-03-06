from Tile import *  # import Tile, our tile data type
from random import *


# assume tiles have bottom, top, left, right representing their edges, set method setting its type

class Graph:
    def __init__(self, rows, cols):  # number of rows and columns in graph
        self.matrix = []  # eventually will need to initialize the scipy matrix thing
        self.r = rows
        self.c = cols

    def gen(self, tiles,
            choose_function):  # tiles are an array of all possible tiles --> tile types; tried making it able to pass the function for choosing tiles but had some issues
        del self.matrix[:]  # deletes all elements in matrix
        y = 0
        while y < self.r:  # for each row
            self.matrix.append([])  # add empty list for the row --> may need to be different for the matrix
            x = 0
            reset = False
            resets = 0  # number of resets
            while x < self.c:  # for each column
                if reset:  # if we need to reset
                    del self.matrix[y]  # delete the row
                    self.matrix.append([])  # add a new empty row
                    # print("reset")
                    x = 0  # restart indexing for the line
                    resets = resets + 1  # add one to the resets counter
                    if resets > 4:  # if there were more than four resets
                        if y > 0:  # if we arent in the first row
                            y = y - 2  # go back up two rows (one will get added back so overall go up one)
                            break  # break out of column loop
                reset = False  # set reset to false

                north = None  # north border
                west = None  # left border

                self.matrix[y].append(Tile()) #add new empty tile
                # print(self.matrix, y, x)

                if y > 0:  # if not on the top row
                    north = self.matrix[y - 1][x].bottom()  # get the bottom of the tile above

                if x > 0:  # if not all the way to the left
                    west = self.matrix[y][x - 1].right()  # get the right of the tile to the left

                if north is not None:
                    worksUp = [t for t in tiles if
                               t.borders[
                                   0] is north]  # list of all tiles from the tiles list that work with the north border

                if west is not None:
                    worksLeft = [t for t in tiles if
                                 t.borders[
                                     3] is west]  # list of all tiles from the tiles list that work with the west border

                if north is not None and west is not None:
                    worksBoth = [e for e in worksUp if
                                 e in worksLeft]  # list of tiles that work for both up and down --> list of elements in both
                    # other lists

                if north is not None:  # if there is a northern tile
                    if west is not None:  # if there is a western tile
                        if len(worksBoth) > 0:
                            self.matrix[y][x].set(choose_function(self, worksBoth, self.matrix[y][
                                x - 1]))  # pick tile that works with both borders
                        else:
                            reset = True  # reset the row
                    else:  # no western tile
                        if len(worksUp) > 0:
                            self.matrix[y][x].set(choose_function(self, worksUp, self.matrix[y - 1][
                                x]))  # pick tile that works with upper border
                        else:
                            reset = True  # reset the row
                else:
                    if west is not None:  # if there is a western tile
                        if len(worksLeft) > 0:
                            self.matrix[y][x].set(choose_function(self, worksLeft, self.matrix[y][x - 1]))
                        else:
                            reset = True  # reset the row
                    else:  # no tiles around (only going to happen for the first tile most likely)
                        self.matrix[y][x].set(
                            self.random_choose(tiles, "hi (this param doesn't matter)"))  # choose from any tile
                self.matrix[y][x].isWater()  # have the tile figure out whether or not it is water
                if reset:
                    x = -1
                x = x + 1
            y = y + 1

    def random_choose(self, tiles,
                      tile):  # some sort of algorithm for choosing which tile out of the list of possible tiles
        return choice(tiles)

    def abs_similar_choose(self, tiles, tile):  # chooses tiles most similar to a set tile
        least_diff = 10000
        index = randrange(len(tiles))
        for i in range(len(tiles)):
            if tiles[i].abs_edge_difference(tile) < least_diff:
                least_diff = tiles[i].abs_edge_difference(tile)
                index = i
        return tiles[index]

    def abs_different_choose(self, tiles, tile):  # chooses tiles most different from a set tile
        most_diff = 0
        index = randrange(len(tiles))
        for i in range(len(tiles)):
            if tiles[i].abs_edge_difference(tile) > most_diff:
                least_diff = tiles[i].abs_edge_difference(tile)
                index = i
        return tiles[index]

    def signed_similar_choose(self, tiles, tile):  # chooses tiles most similar to a set tile
        least_diff = 10000
        index = randrange(len(tiles))
        for i in range(len(tiles)):
            if tiles[i].signed_edge_difference(tile) < least_diff:
                least_diff = tiles[i].signed_edge_difference(tile)
                index = i
        return tiles[index]

    def signed_different_choose(self, tiles, tile):  # chooses tiles most different from a set tile
        most_diff = 0
        index = randrange(len(tiles))
        for i in range(len(tiles)):
            if tiles[i].signed_edge_difference(tile) > most_diff:
                least_diff = tiles[i].signed_edge_difference(tile)
                index = i
        return tiles[index]

    def display(self):
        for y in range(self.r):
            for x in range(self.c):
                self.matrix[y][x].showBorders()
            print()

    def showWater(self):
        for y in range(self.r):
            for x in range(self.c):
                self.matrix[y][x].showWater()
            print()
