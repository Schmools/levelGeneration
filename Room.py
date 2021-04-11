from Graph import *
from Tile import *


class Room:
    def __init__(self, Tiles, Height=10, Width=10, Tiling=None, Resources=None):
        self.height = Height  # height of room
        self.width = Width  # width of room
        self.tiles = Tiles

        if Tiling is None:  # if no preset tiling
            self.tiling = Graph(self.height, self.width)  # generate a blank graph
            self.tiling.gen(self, self.tiles)  # generate tiling
        else:
            self.tiling = Tiling  # load preset tiling [graph object]

        if Resources is None:  # if no preset Resources matrix
            self.resources = []  # matrix to represent resources
            for i in range(self.height):  # for each # of rows
                self.resources.append([])  # add row
                for j in range(self.width):  # for each # of columns
                    self.resources[i].append(
                        [self.tiling[i][j]])  # add resources from correspodning tile
        else:
            self.resources = Resources

    def get_resource(self, row, col):
        return self.resources[row][col]

    def sync_resources(self, row, col):
        for i in range(self.height):  # for each # of rows
            self.resources.append([])  # add row
            for j in range(self.width):  # for each # of columns
                self.resources[i].append(
                    [self.tiling[i][j]])  # add resources from correspodning tile