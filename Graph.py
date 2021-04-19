from Tile import *  # import Tile, our tile data type


# assume tiles have bottom, top, left, right representing their edges, set method setting its type

class Graph:
    def __init__(self, rows, cols):  # number of rows and columns in graph
        self.matrix = []  # eventually will need to initialize the scipy matrix thing
        self.r = rows
        self.c = cols

    def gen(self, tiles):  # tiles are an array of all possible tiles --> tile types
        del self.graph[:]  # deletes all elements in graph

        for y in range(self.r):  # for each row
            self.map.append([])  # add empty list for the row --> may need to be different for the matrix

            for x in range(self.c):  # for each column
                self.map[y].append(Tile())  # add a new tile

                north = None  # north border
                west = None  # left border

                if y > 0:  # if not on the top row
                    north = self.graph[y - 1][x].bottom()  # get the bottom of the tile above

                if x > 0:  # if not all the way to the left
                    west = self.graph[y][x - 1].right()  # get the right of the tile to the left

                if north is not None:
                    worksUp = [t for t in tiles if
                               t[0] is north]  # list of all tiles from the tiles list that work with the north border

                if west is not None:
                    worksLeft = [t for t in tiles if
                                 t[3] is west]  # list of all tiles from the tiles list that work with the west border

                if north is not None and west is not None:
                    worksBoth = list(set(worksUp)).intersection(set(
                        worksLeft))  # list of tiles that work for both up and down --> list of elements in both
                    # other lists

                if north is not None:  # if there is a northern tile
                    if west is not None:  # if there is a western tile
                        self.map[y][x].set(self.choose(worksBoth))  # pick tile that works with both borders
                    else:  # no western tile
                        self.map[y][x].set(self.choose(worksUp))  # pick tile that works with upper border
                else:
                    if west is not None:  # if there is a western tile
                        self.map[y][x].set(self.choose(worksLeft))
                    else:  # no tiles around (only going to happen for the first tile most likely)
                        self.map[y][x].set(self.choose(tiles))  # choose from any tile

    def choose(self):  # some sort of algorithm for choosing which tile out of the list of possible tiles
        pass
